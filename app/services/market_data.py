from typing import List

import httpx
from bs4 import BeautifulSoup

from app.core.http_client import get_async_client
from app.models.market_item import MarketItem

DUCKDUCKGO_NEWS_URL = "https://duckduckgo.com/html/"


async def fetch_market_news(sector: str) -> List[MarketItem]:
    query = f"India {sector} market news"
    params = {
        "q": query,
        "kl": "in-en",
    }

    items: List[MarketItem] = []

    try:
        async with get_async_client() as client:
            response = await client.get(DUCKDUCKGO_NEWS_URL, params=params)
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select(".result__body")[:5]

        for r in results:
            title_el = r.select_one(".result__a")
            snippet_el = r.select_one(".result__snippet")

            if not title_el:
                continue

            items.append(
                MarketItem(
                    title=title_el.get_text(strip=True),
                    source="DuckDuckGo",
                    url=title_el["href"],
                    summary=snippet_el.get_text(strip=True) if snippet_el else None,
                    published_at=None,
                )
            )

    except httpx.HTTPError:
        # Fail silently caller method decides how to proceed
        return []

    return items
