To test the FastAPI application, we can use FastAPI's TestClient which allows us to simulate WebSocket communication. We can use Pytest for our test framework. 

Firstly, let's import necessary modules and initialize the FastAPI TestClient:

```python
from fastapi.testclient import TestClient
from fastapi import FastAPI
from app import app, Direction, Player

client = TestClient(app)
```

Let's start with a test case for successful WebSocket connection and data transfer:

```python
def test_websocket_connection():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(Direction.right.value)
        data = websocket.receive_text()
        assert data == "Player moved right"
```

We can also test if the WebSocket connection handles invalid directions correctly:

```python
def test_websocket_invalid_direction():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("invalidDirection")
        data = websocket.receive_text()
        assert data == "Invalid direction"
```

Next, we can test if the player's coordinates are updated correctly. However, this will require that we expose the player's coordinates through an additional endpoint:

```python
@app.get("/player")
def get_player():
    """Get the player's coordinates"""
    return {"x": player.x, "y": player.y}
```

Now, we can write a test for this:

```python
def test_player_movement():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(Direction.right.value)
        websocket.send_text(Direction.up.value)
        data = client.get("/player").json()
        assert data == {"x": 1, "y": 1}
```

Lastly, let's add a test case for an edge case where the WebSocket connection is closed unexpectedly:

```python
def test_websocket_connection_closed():
    with pytest.raises(WebSocketDisconnect):
        with client.websocket_connect("/ws") as websocket:
            websocket.send_text(Direction.right.value)
            websocket.close()
            websocket.send_text(Direction.up.value)
```

In these tests, we covered all possible scenarios including success cases, error cases, data validation, and edge cases.