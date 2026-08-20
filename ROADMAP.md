# 10-Week Development Roadmap

## Week 1 - Project Initialization
- Finalize project scaffold and development tooling
- Confirm local environment (Python, Docker, Ollama, Qdrant)
- Establish coding conventions and branching workflow

## Week 2 - FastAPI Foundations
- Implement and validate Todo API learning module
- Add centralized config and shared data models
- Expand route structure with health + placeholder APIs

## Week 3 - GitHub Integration (Phase 3)
- Add authenticated GitHub client wrapper
- Implement repository metadata and issue/PR fetch
- Handle pagination and rate-limit scenarios

## Week 4 - Data Processing
- Design text normalization and chunking pipeline
- Add ingestion preparation layer for repository artifacts
- Define canonical document schema for storage

## Week 5 - Embeddings + Vector Store (Phase 4)
- Integrate sentence-transformers embeddings pipeline
- Add Qdrant collection lifecycle management
- Implement upsert and retrieval primitives

## Week 6 - RAG Chain (Phase 5)
- Build retrieval + prompt orchestration
- Integrate Ollama model inference through LangChain
- Add baseline answer quality checks

## Week 7 - Search/Ingress APIs (Phase 6)
- Implement semantic search endpoint
- Implement repository ingest endpoint
- Add duplicate issue detection endpoint

## Week 8 - Frontend Workflow
- Build Streamlit screens for ingestion/search/check workflows
- Add response visualization and action controls
- Improve UX for issue resolution flow

## Week 9 - Reliability + Testing
- Add integration tests for API and retrieval flow
- Add performance and failure-mode checks
- Tighten logging, error handling, and observability

## Week 10 - Hardening + Release
- Run end-to-end validation on target repositories
- Finalize deployment strategy and docs
- Prepare release checklist and future Phase 2+ backlog
