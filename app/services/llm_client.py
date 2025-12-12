import httpx

from app.core.config import settings

GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"


class LLMClientError(Exception):
    pass


async def call_gemini(prompt: str) -> str:
    if not settings.api_token:
        raise LLMClientError("Gemini API key not configured")

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    params = {
        "key": settings.api_token,
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                GEMINI_ENDPOINT,
                params=params,
                json=payload,
            )
            response.raise_for_status()

        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as exc:
        raise LLMClientError(str(exc)) from exc
