# GitHub Issue Resolution Assistant

An AI-powered developer assistant that indexes GitHub repository history and enables semantic search across issues, pull requests, and commits. Engineers can ask natural language questions like "Has this bug occurred before?" and receive instant answers with proven fixes and direct links to related commits and PRs.

## The Problem

Software developers waste significant time debugging issues that have likely been encountered before. Manual searching through GitHub issues lacks semantic understanding, often missing related problems reported with different terminology. This creates duplicate work, slows down issue resolution, and prevents teams from leveraging their institutional knowledge.

## The Solution

This platform automatically crawls and indexes a repository's complete history—issues, PRs, commits, and documentation—building a searchable knowledge base powered by semantic embeddings and LLM reasoning. Developers get intelligent answers backed by real historical context.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Streamlit Frontend                         │
│            (Issue Search, Ingest, Duplicate Detection)          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│                      FastAPI Backend                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ GitHub API   │  │  Embeddings  │  │  RAG Chain (LLM)     │  │
│  │  Integration │  │  (Transformers)  │  (LangChain)         │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└──────────────────────────┬─────────────────────��────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Ollama     │  │   Qdrant     │  │  GitHub API  │
│  (LLM Local) │  │ (Vector DB)  │  │  (Real-time) │
└──────────────┘  └──────────────┘  └──────────────┘
```

## Core Features (In Development)

- **Semantic Issue Search** — Find similar issues using vector embeddings, not just keywords
- **Fix & Resolution Retrieval** — Automatically extract linked PRs, closing commits, and resolution details
- **Duplicate Detection** — Identify potential duplicate issues before they're filed
- **Commit Link Tracer** — Extract and link commits that reference issues (e.g., `fixes #123`)
- **Documentation Cross-Reference** — Surface README, wiki, and contributing guide sections relevant to the issue
- **Auto-Summary Generation** — LLM-powered summaries of past occurrences and fixes
- **Multi-Repository Support** — Index and search across multiple repositories

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI, Pydantic, Python 3.11+ |
| **Frontend** | Streamlit |
| **LLM Orchestration** | LangChain, LangChain Expression Language (LCEL) |
| **Vector Database** | Qdrant |
| **Text Embeddings** | Sentence Transformers |
| **Local LLM Inference** | Ollama (qwen2.5-coder, llama3.1) |
| **GitHub Integration** | PyGithub |
| **Testing** | Pytest |
| **Containerization** | Docker, Docker Compose |

## Current Implementation Status

✅ **Completed**
- FastAPI REST framework with CORS support
- Pydantic data models and request/response validation
- Environment-based configuration management
- Docker Compose stack (Ollama + Qdrant + Backend + Frontend)
- Comprehensive test suite with 4/4 tests passing
- Health check and root endpoints
- Modular route structure for upcoming features

🚧 **In Progress**
- GitHub repository crawler (PyGithub integration)
- Text embedding pipeline (Sentence Transformers)
- Qdrant vector store management
- LangChain RAG chain orchestration
- Semantic search API endpoint
- Repository ingestion pipeline
- Duplicate detection algorithm

## Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Ollama (for local LLM)
- 16+ GB RAM recommended

### Installation

1. **Clone and setup:**
   ```bash
   git clone https://github.com/aditya-dhiman-07/github-issue-assistant.git
   cd github-issue-assistant
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GitHub token
   ```

4. **Start services:**
   ```bash
   docker compose up -d qdrant ollama
   ```

5. **Run backend:**
   ```bash
   uvicorn backend.main:app --reload
   ```
   Visit: http://localhost:8000/docs for interactive API documentation

6. **Run frontend (optional):**
   ```bash
   streamlit run frontend/app.py
   ```

### Full Stack with Docker

```bash
docker compose up --build
```

Services will be available at:
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:8501
- Qdrant: http://localhost:6333
- Ollama: http://localhost:11434

## API Endpoints (Current)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service health check |
| GET | `/health` | Detailed health status |
| GET | `/todos` | List all todos (demo endpoint) |
| POST | `/todos` | Create new todo (demo endpoint) |

## Testing

Run all tests:
```bash
pytest tests/
```

Run with verbose output:
```bash
pytest tests/ -v
```

## Development Workflow

1. Create feature branch from main
2. Implement feature with meaningful commits
3. Add tests in `tests/` directory
4. Ensure all tests pass locally
5. Push and create pull request

## Project Roadmap

### Immediate Next Steps
1. **GitHub Integration** — Implement repository crawler using PyGithub
2. **Data Processing** — Build text chunking and normalization pipeline
3. **Vector Store** — Integrate Qdrant for semantic storage and retrieval
4. **Embeddings** — Set up Sentence Transformers for text vectorization
5. **RAG Pipeline** — Build LangChain chain for LLM reasoning
6. **Search APIs** — Implement semantic search, ingest, and duplicate detection endpoints
7. **Frontend UI** — Build Streamlit workflows
8. **Production Ready** — Testing, optimization, and deployment

## Environment Variables

Create `.env` file with:
```env
GITHUB_TOKEN=your_github_token_here
OLLAMA_BASE_URL=http://localhost:11434
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

## Key Dependencies

```
fastapi==0.104.1              # Web framework
uvicorn[standard]==0.24.0     # ASGI server
pydantic==2.5.0               # Data validation
pydantic-settings==2.1.0      # Config management

langchain==0.1.1              # LLM orchestration
langchain-ollama              # Ollama integration
qdrant-client==2.7.0          # Vector database
PyGithub==2.1.1               # GitHub API
sentence-transformers==2.2.2  # Text embeddings

streamlit==1.28.1             # Frontend framework
pytest==7.4.3                 # Testing
```

## Code Quality

- Type hints throughout codebase
- Pydantic validation for all API inputs
- Comprehensive error handling
- Test-driven development practices
- Clean architecture with separation of concerns

## License

MIT

## Contributing

Contributions are welcome. Please ensure:
- All tests pass locally before pushing
- Code follows project conventions
- Commit messages describe actual functionality changes
- No breaking changes to existing APIs

## Support

For issues, questions, or feature requests, please open a GitHub issue in this repository.

---

**Status:** Active Development | **Last Updated:** August 2026
