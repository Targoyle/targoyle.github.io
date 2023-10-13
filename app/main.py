import os
import sys

sys.path.append(os.environ.get("APP_PATH"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import default

app = FastAPI(
    title="Vercel FastAPI",
    description="[targoyle.github.io](https://targoyle.github.io)",
    version="0.0.1",
    root_path="/",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

allow_origins = os.environ.get("ALLOW_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(default.router)
