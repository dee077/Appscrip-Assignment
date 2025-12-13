from typing import List

from app.core.utils import now_ist
from app.models.market_item import MarketItem
from app.services.llm_client import LLMClientError, call_gemini


def build_prompt(sector: str, items: List[MarketItem]) -> str:
    """Build a strict, guardrailed prompt for the LLM. The model is explicitly forbidden from hallucinating."""

    if not items:
        context = "No recent news items were found."
    else:
        context = "\n".join(
            f"- {item.title}: {item.summary or 'No summary available'}"
            for item in items
        )

    return f"""
    You are a market analyst specializing in Indian sectoral markets.

    Analyze the {sector} sector in India using ONLY the information provided below.

    Rules:
    - Do NOT invent facts or data.
    - If information is insufficient, explicitly say so.
    - Do NOT add external knowledge.
    - Respond ONLY in valid Markdown.
    - Use the EXACT structure below.

    Required Structure:
    ## Market Summary
    ## Key Developments
    ## Trade Opportunities
    ## Risks

    Market Information:
    {context}
    """.strip()


async def analyze_market(
    sector: str,
    items: List[MarketItem],
) -> str:
    """Orchestrates market analysis. Falls back gracefully if LLM fails or data is insufficient."""

    if not items:
        return fallback_no_data_report(sector)

    try:
        analysis = await call_gemini(build_prompt(sector, items))
    except LLMClientError:
        return fallback_llm_error_report(sector, items)

    return render_markdown(sector, analysis, items)


def render_markdown(
    sector: str,
    analysis: str,
    items: List[MarketItem],
) -> str:
    """Final Markdown renderer. Enforces metadata and data source listing."""

    return f"""# Market Analysis — {sector.title()}

**Generated at:** {now_ist().isoformat()}

{analysis}

## Data Sources
""" + "\n".join(
        f"- [{item.title}]({item.url})" for item in items
    )


def fallback_no_data_report(sector: str) -> str:
    """Used when no market data could be collected. This is NOT an error condition."""

    return f"""# Market Analysis — {sector.title()}

**Generated at:** {now_ist().isoformat()}

## Market Summary
No reliable recent market data was found for the Indian {sector} sector.

## Key Developments
No verified developments could be identified at this time.

## Trade Opportunities
Trade opportunities cannot be evaluated without current market signals.

## Risks
- Acting without up-to-date information
- Incomplete market visibility

## Data Sources
- DuckDuckGo News
"""


def fallback_llm_error_report(
    sector: str,
    items: List[MarketItem],
) -> str:
    """Used when Gemini fails but market data exists."""

    return (
        f"""# Market Analysis — {sector.title()}

**Generated at:** {now_ist().isoformat()}

## Market Summary
Automated AI analysis is temporarily unavailable.
Below are the raw market signals collected.

## Market Signals
"""
    + "\n".join(f"- {item.title}" for item in items)
    + """

## Trade Opportunities
Manual interpretation required due to AI unavailability.

## Risks
- Reduced analytical depth
- Potential missed correlations

## Data Sources
"""
        + "\n".join(
            f"- [{item.title}]({item.url})" for item in items
        )
    )
