To tackle this task, we need to create an API endpoint that handles the game logic for ghosts chasing Pac-Man. This endpoint will take the positions of the ghosts and Pac-Man as input, and return the new positions of the ghosts.

Let's start by defining the Pydantic models for our request and response:

```python
from pydantic import BaseModel
from typing import List, Tuple

class Position(BaseModel):
    x: int
    y: int

class GameInput(BaseModel):
    pacman: Position
    ghosts: List[Position]

class GameOutput(BaseModel):
    ghosts: List[Position]
```

Next, let's create the service layer that handles the game logic:

```python
class GameService:
    @staticmethod
    def move_ghosts(input: GameInput) -> GameOutput:
        """ The logic for moving the ghosts toward Pac-Man """
        # This is just a very simple algorithm for demonstration.
        # In a real world scenario, this would be much more complex.
        for ghost in input.ghosts:
            if ghost.x < input.pacman.x:
                ghost.x += 1
            elif ghost.x > input.pacman.x:
                ghost.x -= 1

            if ghost.y < input.pacman.y:
                ghost.y += 1
            elif ghost.y > input.pacman.y:
                ghost.y -= 1

        return GameOutput(ghosts=input.ghosts)
```

Now, we can create our FastAPI application and define our API endpoint:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/game/move-ghosts", response_model=GameOutput)
async def move_ghosts(input: GameInput):
    """ Move ghosts toward Pac-Man """
    return GameService.move_ghosts(input)
```

This endpoint is using POST method as it's modifying the state of the game.

Finally, let's write a unit test for our endpoint:

```python
from fastapi.testclient import TestClient

def test_move_ghosts():
    client = TestClient(app)
    response = client.post(
        "/game/move-ghosts",
        json={
            "pacman": {"x": 5, "y": 5},
            "ghosts": [
                {"x": 1, "y": 1},
                {"x": 9, "y": 9},
                {"x": 5, "y": 1}
            ]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "ghosts": [
            {"x": 2, "y": 2},
            {"x": 8, "y": 8},
            {"x": 5, "y": 2}
        ]
    }
```

Note: This is a simplification of the game logic and does not include error handling and logging, authentication/authorization, and collision detection. These topics would each require their own detailed explanation.