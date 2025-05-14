Here are the unit tests for success cases, error cases, data validation, and edge cases. In this example, we are using pytest for writing unit tests:

```python
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

@pytest.fixture
def valid_game_input():
    return {
        "pacman": {"x": 5, "y": 5},
        "ghosts": [
            {"x": 1, "y": 1},
            {"x": 9, "y": 9},
            {"x": 5, "y": 1}
        ]
    }

@pytest.fixture
def invalid_game_input():
    return {
        "pacman": {"x": "invalid", "y": 5},
        "ghosts": [
            {"x": 1, "y": 1},
            {"x": 9, "y": 9},
            {"x": 5, "y": 1}
        ]
    }

def test_move_ghosts_success(valid_game_input):
    response = client.post("/game/move-ghosts", json=valid_game_input)
    assert response.status_code == 200
    assert response.json() == {
        "ghosts": [
            {"x": 2, "y": 2},
            {"x": 8, "y": 8},
            {"x": 5, "y": 2}
        ]
    }

def test_move_ghosts_error(invalid_game_input):
    response = client.post("/game/move-ghosts", json=invalid_game_input)
    assert response.status_code == 422
    assert "value_error" in response.json()["detail"][0]["type"]

def test_move_ghosts_data_validation():
    # Missing required data
    response = client.post("/game/move-ghosts", json={})
    assert response.status_code == 422
    assert "value_error.missing" in response.json()["detail"][0]["type"]

def test_move_ghosts_edge_case():
    # Pacman and ghosts are in the same position
    response = client.post("/game/move-ghosts", json={
        "pacman": {"x": 1, "y": 1},
        "ghosts": [{"x": 1, "y": 1}]
    })
    assert response.status_code == 200
    assert response.json() == {"ghosts": [{"x": 1, "y": 1}]}
```

In these tests, we are using pytest fixtures to create valid and invalid game inputs. The `valid_game_input` is used for the success case test, while `invalid_game_input` is used for the error case test. 

In the data validation test, we are testing if the endpoint correctly handles requests that are missing required data. 

The edge case test checks if the endpoint correctly handles the situation where Pac-Man and the ghosts are in the same position. In this simplistic game logic, the ghosts will not move if they are in the same position as Pac-Man.