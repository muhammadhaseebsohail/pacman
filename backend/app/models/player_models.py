In our API endpoints, we are already using Pydantic models for request and response. Here is a detailed breakdown:

1. Request Models: 

```python
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

In the `create_player` and `create_ghost` endpoints, `Player` and `Ghost` models are used as request bodies.

2. Response Models:

```python
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

In the `create_player`, `create_ghost`, `get_player`, and `move_player` endpoints, `Player` and `Ghost` models are used as response bodies.

3. Data Transfer Objects:

In this case, our Pydantic models are acting as Data Transfer Objects (DTOs) as well. They are used to transfer data between processes or components. 

In this game logic, we are using DTOs to transfer data between the client and the server, and also between different components of the server. The `Player` and `Ghost` models carry the data about the state of each player and ghost, including their current position and the number of lives a player has. 

To be more precise, when we create a new player or ghost, we use these DTOs to carry the data from the client to the server. When we move a player or check a player's status, we use these DTOs to carry the data from the server back to the client.