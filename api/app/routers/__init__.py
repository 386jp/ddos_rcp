# Import Libraries
from fastapi import APIRouter

# FastAPI settings
router = APIRouter()

# Import routes

from app.routers import gamemgr
router.include_router(gamemgr.router, prefix="/gamemgr", tags=["gamemgr"],)

from app.routers import game
router.include_router(game.router, prefix="/game", tags=["game"],)

from app.routers import result
router.include_router(result.router, prefix="/result", tags=["result"],)