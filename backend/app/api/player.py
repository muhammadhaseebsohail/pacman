Sure, let's create a game backend where we will have an endpoint that advances the level or restarts it when all dots are eaten. 

First, let's define our Pydantic models:

```python
from pydantic import BaseModel
from typing import Optional

class Level(BaseModel):
    number: int
    dots_remaining: int
    is_completed: Optional[bool] = False

class Player(BaseModel):
    name: str
    current_level: int
    score: int
```
The Level model represents the game level with the number of the level, the dots remaining and if the level is completed or not.

The Player model represents the player with their name, their current level in the game, and their total score.

Now, let's create the FastAPI endpoint:

```python
from fastapi import FastAPI, HTTPException, status
from typing import Dict

app = FastAPI()

# In-memory storage for simplicity
players: Dict[str, Player] = {}
levels: Dict[int, Level] = {}

@app.post("/player/", response_model=Player)
def create_player(player: Player):
    """Create a new player"""
    players[player.name] = player
    return player

@app.post("/level/", response_model=Level)
def create_level(level: Level):
    """Create a new game level"""
    levels[level.number] = level
    return level

@app.get("/level/{level_number}/", response_model=Level)
def get_level(level_number: int):
    """Get the details of a game level"""
    if level_number not in levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
    return levels[level_number]

@app.put("/level/{level_number}/", response_model=Level)
def update_level(level_number: int, level: Level):
    """Update a game level"""
    if level_number not in levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
    levels[level_number] = level
    return level

@app.post("/player/{player_name}/eat_dot/")
def eat_dot(player_name: str):
    """Player eats a dot on their current level"""
    if player_name not in players:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    player = players[player_name]
    level = levels[player.current_level]
    if level.dots_remaining > 0:
        level.dots_remaining -= 1
        if level.dots_remaining == 0:
            level.is_completed = True
            player.current_level += 1
        player.score += 10
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No dots remaining in this level")
    return {"msg": "Dot eaten successfully!"}
```

This code defines an API with endpoints for creating players and levels, getting a level's details, updating a level, and eating a dot in a level. When a player eats a dot on their current level, the number of dots remaining in the level is decreased. If there are no more dots, the level is marked as completed and the player's current level is increased. 

For simplicity, I've used in-memory storage to store the players and levels, but in a real application, you'd likely use a database.

And finally, for unit tests, we could do something like:
```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_player():
    response = client.post("/player/", json={"name": "test_player", "current_level": 1, "score": 0})
    assert response.status_code == 200
    assert response.json() == {"name": "test_player", "current_level": 1, "score": 0}

def test_create_level():
    response = client.post("/level/", json={"number": 1, "dots_remaining": 10, "is_completed": False})
    assert response.status_code == 200
    assert response.json() == {"number": 1, "dots_remaining": 10, "is_completed": False}

def test_eat_dot():
    response = client.post("/player/test_player/eat_dot/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Dot eaten successfully!"}
```

These tests verify that the endpoints for creating players and levels and eating a dot work as expected.