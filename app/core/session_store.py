from typing import Dict

from app.core.utils import now_ist
from app.models.session import Session


class SessionStore:
    def __init__(self):
        self._sessions: Dict[str, Session] = {}

    def create(self, token: str) -> Session:
        now = now_ist()
        session = Session(
            token=token,
            created_at=now,
            last_used_at=now,
            window_start=now,
            request_count=0,
        )
        self._sessions[token] = session
        return session

    def get(self, token: str) -> Session | None:
        session = self._sessions.get(token)
        if session:
            session.last_used_at = now_ist()
        return session
