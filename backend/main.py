"""FastAPI app entrypoint with a Todo API learning foundation."""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from backend.models import Todo, TodoCreate
from backend.routes import duplicate_check, health, ingest, search

app = FastAPI(
    title="GitHub Issue Resolution Assistant API",
    description="Phase 2 learning foundation with Todo API and modular route scaffolding.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(search.router)
app.include_router(ingest.router)
app.include_router(duplicate_check.router)

TODOS: list[Todo] = []
NEXT_TODO_ID = 1


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "GitHub Issue Resolution Assistant backend is running."}


@app.get("/todos", response_model=list[Todo], tags=["todos"])
def list_todos() -> list[Todo]:
    return TODOS


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["todos"])
def add_todo(todo: TodoCreate) -> Todo:
    global NEXT_TODO_ID

    if any(existing.title.lower() == todo.title.lower() for existing in TODOS):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Todo with this title already exists")

    created = Todo(id=NEXT_TODO_ID, title=todo.title, completed=todo.completed)
    TODOS.append(created)
    NEXT_TODO_ID += 1
    return created
