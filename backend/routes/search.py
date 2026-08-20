"""Phase 6 semantic search route stub."""

from fastapi import APIRouter

from backend.models import StubResponse

router = APIRouter(prefix="/search", tags=["search"])


@router.get("", response_model=StubResponse)
def semantic_search() -> StubResponse:
    return StubResponse(message="Phase 6 stub: semantic search endpoint not implemented yet.")
