Here are the unit tests for the FastAPI endpoints:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_player():
    response = client.post("/player", json={"id": 1, "x": 0, "y": 0, "lives": 3})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "x": 0, "y": 0, "lives": 3}

def test_create_ghost():
    response = client.post("/ghost", json={"id": 1, "x": 1, "y": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "x": 1, "y": 1}

def test_get_player():
    client.post("/player", json={"id": 1, "x": 0, "y": 0, "lives": 3})
    response = client.get("/player/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "x": 0, "y": 0, "lives": 3}

def test_get_player_not_found():
    response = client.get("/player/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Player not found"}

def test_move_player():
    client.post("/player", json={"id": 1, "x": 0, "y": 0, "lives": 3})
    client.post("/ghost", json={"id": 1, "x": 1, "y": 1})
    response = client.post("/player/1/move", json={"x": 1, "y": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "x": 1, "y": 1, "lives": 2}

def test_move_player_out_of_lives():
    client.post("/player", json={"id": 1, "x": 0, "y": 0, "lives": 1})
    client.post("/ghost", json={"id": 1, "x": 1, "y": 1})
    response = client.post("/player/1/move", json={"x": 1, "y": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Game Over"}

def test_move_player_invalid_coordinates():
    response = client.post("/player/1/move", json={"x": "invalid", "y": "invalid"})
    assert response.status_code == 422
```

These tests cover:
- Success cases: creating a player, creating a ghost, getting a player, and moving a player.
- Error cases: getting a non-existent player, moving a player with invalid coordinates.
- Data validation: Pydantic validates the input data for us. If we try to move a player with invalid coordinates, Pydantic will return a 422 Unprocessable Entity response.
- Edge cases: moving a player when they have no more lives.