import httpx

DEFAULT_TIMEOUT = 10.0


def get_async_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        timeout=httpx.Timeout(DEFAULT_TIMEOUT),
        headers={"User-Agent": "Trade-Opportunities-API/1.0"},
    )
