Here's a basic implementation of your requirements. I'm going to use an in-memory store for simplicity, but you could replace it with a database or other persistent storage.

First, let's set up our models:

```python
from pydantic import BaseModel
from enum import Enum

class State(str, Enum):
    NORMAL = "normal"
    VULNERABLE = "vulnerable"

class Ghost(BaseModel):
    id: int
    state: State = State.NORMAL

class Pacman(BaseModel):
    id: int
    position: dict

class PowerPellet(BaseModel):
    id: int
    position: dict
```

Now, let's create our main FastAPI application:

```python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# In-memory stores
pacmen = []
ghosts = []
power_pellets = []

@app.post("/pacmen/", response_model=Pacman)
def create_pacman(pacman: Pacman):
    """
    Create a new Pacman.
    """
    pacmen.append(pacman)
    return pacman

@app.post("/ghosts/", response_model=Ghost)
def create_ghost(ghost: Ghost):
    """
    Create a new Ghost.
    """
    ghosts.append(ghost)
    return ghost

@app.post("/power_pellets/", response_model=PowerPellet)
def create_power_pellet(power_pellet: PowerPellet):
    """
    Create a new Power Pellet.
    """
    power_pellets.append(power_pellet)
    return power_pellet

@app.put("/pacmen/{pacman_id}")
def eat_pellet(pacman_id: int):
    """
    Pacman eats a power pellet.
    """
    for pacman in pacmen:
        if pacman.id == pacman_id:
            for power_pellet in power_pellets:
                if pacman.position == power_pellet.position:
                    power_pellets.remove(power_pellet)
                    for ghost in ghosts:
                        ghost.state = State.VULNERABLE
                    return {"message": "Power pellet eaten, ghosts are now vulnerable!"}
            raise HTTPException(status_code=404, detail="Power pellet not found at Pacman's position.")
    raise HTTPException(status_code=404, detail="Pacman not found.")
```

Finally, let's write some tests:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_eat_pellet():
    response = client.post("/pacmen/", json={"id": 1, "position": {"x": 10, "y": 20}})
    assert response.status_code == 200
    response = client.post("/power_pellets/", json={"id": 1, "position": {"x": 10, "y": 20}})
    assert response.status_code == 200
    response = client.put("/pacmen/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Power pellet eaten, ghosts are now vulnerable!"}
```

Please note that this is a basic implementation and doesn't cover all edge cases. For example, it doesn't handle if there are multiple Pacman or Ghost instances, and it doesn't reset the Ghost state after a certain period. You'd need to add these features according to your game's rules.