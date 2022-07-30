from typing import TYPE_CHECKING, Optional, List
from enum import Enum
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from app.models import Result

class GameBase(SQLModel):
    # room_id: Optional[int] = Field(nullable=True)
    pass

class Game(GameBase, table=True):
    id: Optional[int] = Field(primary_key=True, nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    results: Optional[List["Result"]] = Relationship(back_populates="game")

class GameCreate(GameBase):
    pass

class GameRead(GameBase):
    id: int
    created_at: datetime
    updated_at: datetime

class GameUpdate(SQLModel):
    pass