from datetime import datetime

from pydantic import BaseModel, HttpUrl


class MarketItem(BaseModel):
    title: str
    source: str
    url: HttpUrl
    published_at: datetime | None = None
    summary: str | None = None
