from datetime import timedelta

from fastapi import HTTPException, status

from app.core.config import settings
from app.core.utils import now_ist
from app.models.session import Session


def enforce_rate_limit(session: Session) -> None:
    now = now_ist()
    window_duration = timedelta(seconds=settings.rate_limit_window_seconds)

    if now - session.window_start >= window_duration:
        session.window_start = now
        session.request_count = 0

    session.request_count += 1

    if session.request_count > settings.rate_limit_requests:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Try again later.",
            headers={
                "Retry-After": str(settings.rate_limit_window_seconds),
            },
        )
