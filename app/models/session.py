from datetime import datetime

from pydantic import BaseModel


class Session(BaseModel):
    token: str
    created_at: datetime
    last_used_at: datetime

    window_start: datetime
    request_count: int = 0
