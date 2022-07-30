import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
import app.env as env

# Load environment variables
load_dotenv()

tags_metadata = [
    {
        "name": "gamemgr",
        "description": "じゃんけんを行うAPIエンドポイント",
    },
]

app = FastAPI(
    title = "ddos_rcp",
    description = "RCP API Demo for DDoS 2022",
    version = env.API_VERSION,
    openapi_tags=tags_metadata,
    root_path = "/" if os.getenv("DEV_MODE", 'False') == 'True' else "/api",
    openapi_url = '/openapi.json' if os.getenv("DEV_MODE", 'False') == 'True' else None,
    debug = True if os.getenv("DEV_MODE", 'False') == 'True' else False,
    )

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"] if os.getenv("DEV_MODE", 'False') == 'True' else origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(router)

logger = logging.getLogger('uvicorn')