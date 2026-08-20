from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_todos_initially_empty() -> None:
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo() -> None:
    response = client.post("/todos", json={"title": "Learn FastAPI", "completed": False})
    assert response.status_code == 201
    assert response.json()["id"] >= 1
    assert response.json()["title"] == "Learn FastAPI"


def test_duplicate_todo_returns_conflict() -> None:
    client.post("/todos", json={"title": "Unique Task", "completed": False})
    duplicate = client.post("/todos", json={"title": "unique task", "completed": False})
    assert duplicate.status_code == 409
