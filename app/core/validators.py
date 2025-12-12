import re

from fastapi import HTTPException, status

ALLOWED_SECTORS = {
    "pharmaceuticals",
    "technology",
    "agriculture",
    "finance",
    "energy",
    "manufacturing",
}


def validate_sector(sector: str) -> str:
    normalized = sector.strip().lower()

    if not normalized:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sector cannot be empty",
        )

    if len(normalized) > 50:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sector name too long",
        )

    if not re.fullmatch(r"[a-z ]+", normalized):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sector contains invalid characters",
        )

    if normalized not in ALLOWED_SECTORS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported sector: {normalized}",
        )

    return normalized
