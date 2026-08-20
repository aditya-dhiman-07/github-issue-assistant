"""Phase 6 ingestion route stub."""

from fastapi import APIRouter

from backend.models import StubResponse

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("", response_model=StubResponse)
def ingest_repository() -> StubResponse:
    return StubResponse(message="Phase 6 stub: repository ingestion endpoint not implemented yet.")
