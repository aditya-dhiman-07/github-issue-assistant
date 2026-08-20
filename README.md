# GitHub Issue Resolution Assistant

GitHub Issue Resolution Assistant is a phased project that helps ingest repository context, retrieve relevant knowledge with semantic search, and assist in triaging or resolving GitHub issues.

## Project Overview

This repository provides a production-ready scaffold for the first two phases:

- **Phase 1:** environment-ready project layout and configuration
- **Phase 2:** a working FastAPI Todo API foundation for learning and extension

## Architecture (high-level)

- **Frontend (Streamlit):** user interface for issue workflows
- **Backend (FastAPI):** API layer, ingestion routes, search routes, and future RAG orchestration
- **Ollama:** local LLM inference endpoint
- **Qdrant:** vector store for semantic retrieval
- **GitHub API integration:** planned crawler for repository issues/PRs/commits

## Features Included

- Modular backend package structure
- FastAPI app with CORS enabled
- Todo API (`GET /todos`, `POST /todos`) with validation and duplicate protection
- Health endpoint (`GET /health`)
- Placeholder route/module stubs for upcoming phases
- Streamlit frontend stubs
- Docker + docker-compose for local stack
- `.env.example` and centralized settings via `pydantic-settings`
- Test scaffold with route-level examples

## Tech Stack

- Python 3.11+
- FastAPI + Pydantic
- Streamlit
- LangChain ecosystem + Ollama
- Qdrant
- PyGithub
- Pytest
- Docker Compose

## Quick Start

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy environment template:
   ```bash
   cp .env.example .env
   ```
5. Start local infrastructure:
   ```bash
   docker compose up -d qdrant ollama
   ```
6. Run backend API:
   ```bash
   uvicorn backend.main:app --reload
   ```
7. Open API docs:
   - Swagger UI: `http://127.0.0.1:8000/docs`
8. Run frontend stub:
   ```bash
   streamlit run frontend/app.py
   ```

## How to Run Locally (all services)

```bash
docker compose up --build
```

Services:
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:8501`
- Qdrant: `http://localhost:6333`
- Ollama: `http://localhost:11434`

## Development Notes

- Current implementation is intentionally Phase 1-2 focused.
- `backend/github_crawler.py`, `backend/embeddings.py`, `backend/vector_store.py`, and `backend/rag_chain.py` are stubs for upcoming phases.
- Additional route modules under `backend/routes/` are placeholders for semantic search and ingestion workflows.
