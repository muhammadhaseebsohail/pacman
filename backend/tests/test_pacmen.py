Here's how you can write comprehensive unit tests for the above FastAPI endpoint using pytest and FastAPI's TestClient:

```python
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

@pytest.fixture
def setup_data():
    # Setup data for the tests
    client.post("/pacmen/", json={"id": 1, "position": {"x": 10, "y": 20}})
    client.post("/ghosts/", json={"id": 1, "state": "normal"})
    client.post("/power_pellets/", json={"id": 1, "position": {"x": 10, "y": 20}})

def test_create_pacman(setup_data):
    response = client.post("/pacmen/", json={"id": 2, "position": {"x": 15, "y": 25}})
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["position"] == {"x": 15, "y": 25}

def test_create_ghost(setup_data):
    response = client.post("/ghosts/", json={"id": 2, "state": "normal"})
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["state"] == "normal"

def test_create_power_pellet(setup_data):
    response = client.post("/power_pellets/", json={"id": 2, "position": {"x": 15, "y": 25}})
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["position"] == {"x": 15, "y": 25}

def test_eat_pellet_success(setup_data):
    response = client.put("/pacmen/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Power pellet eaten, ghosts are now vulnerable!"}

def test_eat_pellet_fail_no_pacman(setup_data):
    response = client.put("/pacmen/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pacman not found."}

def test_eat_pellet_fail_no_pellet(setup_data):
    client.post("/pacmen/", json={"id": 3, "position": {"x": 15, "y": 25}})
    response = client.put("/pacmen/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Power pellet not found at Pacman's position."}

def test_invalid_pacman_data(setup_data):
    response = client.post("/pacmen/", json={"id": "invalid", "position": {"x": 15, "y": 25}})
    assert response.status_code == 422

def test_invalid_ghost_data(setup_data):
    response = client.post("/ghosts/", json={"id": 2, "state": "invalid"})
    assert response.status_code == 422

def test_invalid_power_pellet_data(setup_data):
    response = client.post("/power_pellets/", json={"id": "invalid", "position": {"x": 15, "y": 25}})
    assert response.status_code == 422
```

This set of unit tests covers:
- Success cases: where the API endpoints function as expected.
- Error cases: where the API endpoints should return error messages.
- Data validation: where the API endpoints should check the input data.
- Edge cases: where the API endpoints should handle exceptional scenarios. In this case, it's when a Pacman tries to eat a power pellet that isn't at their position.