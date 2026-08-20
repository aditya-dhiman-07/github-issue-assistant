"""Phase 6 duplicate detection route stub."""

from fastapi import APIRouter

from backend.models import StubResponse

router = APIRouter(prefix="/duplicate-check", tags=["duplicate-check"])


@router.get("", response_model=StubResponse)
def duplicate_check() -> StubResponse:
    return StubResponse(message="Phase 6 stub: duplicate detection endpoint not implemented yet.")
