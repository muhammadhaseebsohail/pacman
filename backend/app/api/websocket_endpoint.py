Here is an example of how to create an API endpoint for controlling Pac-Man using FastAPI. This example uses WebSocket for real-time communication between the client and the server. Pydantic models are not used here because WebSocket communication typically involves sending and receiving raw data, such as JSON.

```python
from fastapi import FastAPI, WebSocket, HTTPException
from enum import Enum
from typing import Optional

app = FastAPI()

class Direction(str, Enum):
    """Enumeration for Pac-Man movement directions"""
    up = "up"
    down = "down"
    left = "left"
    right = "right"

class Player:
    """Class representing a player"""
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction: Direction):
        """Move the player in a specified direction"""
        if direction == Direction.up:
            self.y += 1
        elif direction == Direction.down:
            self.y -= 1
        elif direction == Direction.left:
            self.x -= 1
        elif direction == Direction.right:
            self.x += 1

player = Player()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Websocket endpoint for controlling Pac-Man"""
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        direction = Direction(data)
        player.move(direction)
        await websocket.send_text(f"Player moved {direction}")
```

In this example, the client would connect to the "/ws" WebSocket endpoint and send text messages to control Pac-Man. The server would interpret these messages as directions and move the player accordingly.

This example does not include error handling, logging, or authentication. In a real-world application, you would want to add these features to ensure the security and reliability of your API. Also, this example does not include any database models or unit tests, as they are not typically used with WebSocket communication.

For example, to add error handling, you could catch exceptions and send an error message back to the client:

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Websocket endpoint for controlling Pac-Man"""
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            direction = Direction(data)
            player.move(direction)
            await websocket.send_text(f"Player moved {direction}")
        except ValueError:
            await websocket.send_text("Invalid direction")
        except Exception as e:
            await websocket.send_text(f"Error: {str(e)}")
```

This would send an "Invalid direction" message if the client sends an invalid direction, and it would send a general error message for any other exceptions.