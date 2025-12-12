import uuid

from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse

from app.core.auth import get_current_session
from app.core.state import session_store
from app.core.validators import validate_sector
from app.services.analyzer import analyze_market
from app.services.market_data import fetch_market_news

router = APIRouter()


@router.get("/", tags=["Status"])
async def status_check():
    return {"status": "ok"}


@router.post("/auth/guest", tags=["Auth"])
async def create_guest_session():
    token = str(uuid.uuid4())
    session = session_store.create(token)
    return {
        "token": session.token,
        "token_type": "Bearer",
    }


@router.get("/protected-test", tags=["Auth"])
async def protected_test(session=Depends(get_current_session)):
    return {
        "message": "Authenticated",
        "token": session.token,
        "created_at": session.created_at,
        "last_used_at": session.last_used_at,
    }


@router.get("/analyze/{sector}", tags=["Analysis"])
async def analyze_sector(
    sector: str,
    session=Depends(get_current_session),
):
    sector = validate_sector(sector)

    market_items = await fetch_market_news(sector)
    report = await analyze_market(sector, market_items)

    return PlainTextResponse(
        content=report,
        media_type="text/markdown",
    )
