In the given code, we have already defined the request models `Player` and `Level` which are used for creating a player and a level respectively. These are also used as response models in their respective endpoints.

However, in the `eat_dot` endpoint, we are returning a simple dictionary message. For consistency and a more defined structure, we can create a response model for this endpoint. Let's call it `DotEaten`:

```python
class DotEaten(BaseModel):
    msg: str
```

And, we can now use it in our `eat_dot` endpoint as follows:

```python
@app.post("/player/{player_name}/eat_dot/", response_model=DotEaten)
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

Now we have a response model for all three endpoints which will provide a more consistent API interface and better type checking.

As for the data transfer objects, the `Player` and `Level` Pydantic models are used for transferring data between the client and the server. If we had a database, we would likely need additional models to map the data to and from the database tables. However, in this case, since we're using in-memory storage, these models are sufficient.