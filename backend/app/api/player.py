For this task, we will need to create some data models, service classes, and API endpoints. I'll define a basic structure for these components. We'll not implement a full game logic but rather focus on collision detection and lives tracking.

1. Pydantic Models:

```python
from pydantic import BaseModel

class Player(BaseModel):
    id: int
    x: int
    y: int
    lives: int

class Ghost(BaseModel):
    id: int
    x: int
    y: int
```

2. Service Layer Code:

```python
from typing import List

class GameService:
    def __init__(self, players: List[Player], ghosts: List[Ghost]):
        self.players = players
        self.ghosts = ghosts

    def detect_collision(self, player_id: int):
        player = next(x for x in self.players if x.id == player_id)
        for ghost in self.ghosts:
            if player.x == ghost.x and player.y == ghost.y:
                player.lives -= 1
                return True
        return False
```

3. API Endpoints:

```python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

game_service = GameService([], [])

@app.post("/player", response_model=Player)
def create_player(player: Player):
    """Create a new player."""
    game_service.players.append(player)
    return player

@app.post("/ghost", response_model=Ghost)
def create_ghost(ghost: Ghost):
    """Create a new ghost."""
    game_service.ghosts.append(ghost)
    return ghost

@app.get("/player/{player_id}", response_model=Player)
def get_player(player_id: int):
    """Get player by ID."""
    try:
        return next(x for x in game_service.players if x.id == player_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Player not found")

@app.post("/player/{player_id}/move", response_model=Player)
def move_player(player_id: int, x: int, y: int):
    """Move a player to a new position."""
    player = get_player(player_id)
    player.x = x
    player.y = y
    if game_service.detect_collision(player_id):
        if player.lives == 0:
            game_service.players.remove(player)
            return {"message": "Game Over"}
    return player
```

4. Unit Tests:

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

def test_move_player():
    client.post("/player", json={"id": 1, "x": 0, "y": 0, "lives": 3})
    client.post("/ghost", json={"id": 1, "x": 1, "y": 1})
    response = client.post("/player/1/move", json={"x": 1, "y": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "x": 1, "y": 1, "lives": 2}
```
Please note that this is a very basic and simplified example of how you might implement your game logic. In a real-world application, you would need to consider additional factors such as multi-threading, handling simultaneous requests, more complex game mechanics, and database storage.