from typing import List
from urllib.parse import urlparse, parse_qs, unquote

import httpx
from bs4 import BeautifulSoup

from app.core.http_client import get_async_client
from app.models.market_item import MarketItem


DUCKDUCKGO_NEWS_URL = "https://html.duckduckgo.com/html/"


async def fetch_market_news(sector: str) -> List[MarketItem]:
    query = f"India {sector} market news"
    params = {
        "q": query,
        "kl": "in-en",
    }

    items: List[MarketItem] = []

    try:
        async with get_async_client() as client:
            response = await client.get(
                DUCKDUCKGO_NEWS_URL,
                params=params,
            )
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        results = soup.select(
            "div.result.web-result div.result__body"
        )[:5]

        for result in results:
            title_el = result.select_one("a.result__a")
            snippet_el = result.select_one("a.result__snippet")

            if not title_el:
                continue

            raw_url = title_el.get("href")
            if not raw_url:
                continue

            if raw_url.startswith("//"):
                raw_url = "https:" + raw_url

            final_url = raw_url
            parsed = urlparse(raw_url)

            if parsed.netloc in {"duckduckgo.com", "www.duckduckgo.com"}:
                qs = parse_qs(parsed.query)
                if "uddg" in qs:
                    final_url = unquote(qs["uddg"][0])

            items.append(
                MarketItem(
                    title=title_el.get_text(strip=True),
                    source="DuckDuckGo",
                    url=final_url,
                    summary=snippet_el.get_text(strip=True) if snippet_el else None,
                    published_at=None,
                )
            )

    except httpx.HTTPError:
        # External failures are not API failures
        return []

    return items
