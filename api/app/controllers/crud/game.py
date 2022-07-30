from typing import List
from datetime import datetime
from fastapi import HTTPException
from app.models import session, Game, GameCreate, GameRead, GameUpdate

from sqlmodel import select

def create_game(game: GameCreate) -> GameRead:
    game_remapped = Game.from_orm(game)
    session.add(game_remapped)
    try:
        session.commit()
    except:
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    else:
        session.refresh(game_remapped)
        return GameRead.from_orm(game_remapped)

def get_games(skip: int = 0, limit: int = 100) -> List[GameRead]:
    games = session.exec(select(Game).order_by(Game.id).offset(skip).limit(limit)).all()
    if len(games) == 0:
        raise HTTPException(status_code=404, detail="Game not found")
    return [GameRead.from_orm(game) for game in games]

def get_game(game_id: int) -> GameRead:
    game = session.get(Game, game_id)
    if game:
        game = GameRead.from_orm(game)
        return game
    else:
        raise HTTPException(status_code=404, detail="Game not found")

def update_game(game_id: int, game: GameUpdate) -> GameRead:
    db_game = session.get(Game, game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    game_data = game.dict(exclude_unset=True)
    for key, value in game_data.items():
        if value is not None:
            setattr(db_game, key, value)
    setattr(db_game, "updated_at", datetime.now())
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    db_game = GameRead.from_orm(db_game)
    return db_game

def delete_game(game_id: int) -> bool:
    game = session.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    session.delete(game)
    session.commit()
    return True