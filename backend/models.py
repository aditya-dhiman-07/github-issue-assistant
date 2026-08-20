"""Pydantic models used by the API."""

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    completed: bool = False


class TodoCreate(TodoBase):
    """Request model for creating a new todo."""


class Todo(TodoBase):
    id: int


class HealthResponse(BaseModel):
    status: str


class StubResponse(BaseModel):
    message: str
