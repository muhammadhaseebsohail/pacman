In this task, you are required to implement the game logic for Pac-Man eating dots to score points. The game logic will consist of a `POST` endpoint that will take in the position for Pac-Man and dots, and return the updated score and the remaining dots. The FastAPI application will be structured as follows:

```python
from fastapi import FastAPI, HTTPException, status
from typing import List
from pydantic import BaseModel
import logging

app = FastAPI(title="Pac-Man Game API")

logger = logging.getLogger('uvicorn.error')

# Pydantic Models
class Dot(BaseModel):
    x: int
    y: int

class PacMan(BaseModel):
    x: int
    y: int

class GameRequest(BaseModel):
    pac_man: PacMan
    dots: List[Dot]

class GameResponse(BaseModel):
    score: int
    remaining_dots: List[Dot]

# Score Keeping
score: int = 0
dots: List[Dot] = []

@app.post("/game", response_model=GameResponse, status_code=status.HTTP_200_OK)
def update_game_state(game_request: GameRequest) -> GameResponse:
    """
    Update the state of the game and calculate the new score.

    - **game_request**: The current positions of Pac-Man and the dots.
    """
    global score
    global dots

    try:
        # Collision Detection
        for dot in game_request.dots:
            if game_request.pac_man.x == dot.x and game_request.pac_man.y == dot.y:
                score += 1
                dots.remove(dot)

        return GameResponse(score=score, remaining_dots=dots)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred.")
```

For this code, the Pydantic models are `Dot`, `PacMan`, `GameRequest`, and `GameResponse`. The models `Dot` and `PacMan` represent the positions of a dot and Pac-Man with `x` and `y` coordinates. The model `GameRequest` is the request body for the `POST` endpoint that takes in the current positions of Pac-Man and the dots. The model `GameResponse` is the response body for the `POST` endpoint that returns the new score and the remaining dots. 

The service layer is handled in the `POST` endpoint `update_game_state`. This function updates the game state and calculates the new score. It does this by iterating over the dots and checking if any of them are at the same position as Pac-Man. If there is a collision, the score is incremented by one and the dot is removed from the remaining dots.

The error handling is done with a try-except block. If an error occurs during the execution of the game logic, an error message is logged and an HTTP Exception with status code 500 is raised. 

There isn't any database model required for this code as all data is kept in memory and not persisted in a database.

The unit tests for this code would test the `POST` endpoint with different inputs to ensure that the game logic is working correctly and that the score and remaining dots are updated correctly. The tests would also check that the endpoint responds with an error when an exception is raised.