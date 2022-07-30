from typing import List
from fastapi import APIRouter

import app.controllers.crud as crud

router = APIRouter()

@router.post("/", response_model=crud.game.GameRead)
def create_game(game: crud.game.GameCreate) -> crud.game.GameRead:
    game_obj = crud.game.create_game(game)
    return crud.game.GameRead.from_orm(game_obj)

@router.get("/", response_model=List[crud.game.GameRead])
def get_games(skip: int=0, limit: int=100) -> List[crud.game.GameRead]:
    game_obj = crud.game.get_games(skip=skip, limit=limit)
    return game_obj

@router.get("/{game_id}", response_model=crud.game.GameRead)
def get_game(game_id: int) -> crud.game.GameRead:
    game_obj = crud.game.get_game(game_id=game_id)
    return game_obj

@router.patch("/{game_id}", response_model=crud.game.GameRead)
def update_game(game_id: int, game: crud.game.GameUpdate) -> crud.game.GameRead:
    game_obj = crud.game.update_game(game_id=game_id, game=game)
    return game_obj

@router.delete("/{game_id}")
def delete_game(game_id: int) -> dict:
    crud.game.delete_game(game_id=game_id)
    return {"status": "success"}