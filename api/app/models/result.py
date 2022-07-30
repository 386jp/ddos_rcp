from typing import Optional
from enum import Enum
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel
from app.models import Game

class RcpChoices(str, Enum):
    ROCK = "ROCK"
    SCISSORS = "SCISSORS"
    PAPER = "PAPER"

class RcpResults(str, Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    DRAW = "DRAW"

class ResultBase(SQLModel):
    game_id: int = Field(default=None, foreign_key="game.id")
    choice: RcpChoices
    result: RcpResults
    is_bot: bool = Field(default=False)

class Result(ResultBase, table=True):
    id: Optional[int] = Field(primary_key=True, nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    game: Optional[Game] = Relationship(back_populates="results")

class ResultCreate(ResultBase):
    pass

class ResultRead(ResultBase):
    id: int
    created_at: datetime
    updated_at: datetime

class ResultUpdate(SQLModel):
    game_id: Optional[int] = None
    choice: Optional[RcpChoices] = None
    result: Optional[RcpResults] = None
    is_bot: Optional[bool] = None