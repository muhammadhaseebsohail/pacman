Let's write comprehensive unit tests for our endpoint using pytest and FastAPI's TestClient.

```python
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

def test_create_player():
    response = client.post("/player/", json={"name": "test_player", "current_level": 1, "score": 0})
    assert response.status_code == 200
    assert response.json() == {"name": "test_player", "current_level": 1, "score": 0}

def test_create_player_no_name():
    response = client.post("/player/", json={"current_level": 1, "score": 0})
    assert response.status_code == 422
    assert "name" in response.json()["detail"][0]["loc"]

def test_create_level():
    response = client.post("/level/", json={"number": 1, "dots_remaining": 10, "is_completed": False})
    assert response.status_code == 200
    assert response.json() == {"number": 1, "dots_remaining": 10, "is_completed": False}

def test_create_level_no_number():
    response = client.post("/level/", json={"dots_remaining": 10, "is_completed": False})
    assert response.status_code == 422
    assert "number" in response.json()["detail"][0]["loc"]

def test_get_level():
    response = client.get("/level/1/")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "dots_remaining": 10, "is_completed": False}

def test_get_level_not_found():
    response = client.get("/level/999/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Level not found"}

def test_eat_dot():
    response = client.post("/player/test_player/eat_dot/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Dot eaten successfully!"}

def test_eat_dot_no_dots_remaining():
    for _ in range(10):  # eat all dots
        client.post("/player/test_player/eat_dot/")
    response = client.post("/player/test_player/eat_dot/")
    assert response.status_code == 400
    assert response.json() == {"detail": "No dots remaining in this level"}

def test_eat_dot_player_not_found():
    response = client.post("/player/non_existent_player/eat_dot/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Player not found"}
```
These tests cover success cases, error cases, data validation, and edge cases. They can be run with pytest.