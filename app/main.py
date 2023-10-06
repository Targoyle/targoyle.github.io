from typing import Dict

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    openapi_url="/openapi.json",  # "/openapi.json" or None
    docs_url="/docs",  # "/docs" or None
    redoc_url="/redoc",  # "/redoc" or None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HelloWorldResponse(BaseModel):
    Hello: str


class EchoResponse(BaseModel):
    headers: Dict[str, str]


@app.get(
    "/",
    summary="Hello World Endpoint",
    description="このエンドポイントは、簡単な 'Hello, World!' メッセージを返却します。",
    response_model=HelloWorldResponse,
)
def hello_world():
    return {
        "Hello": "World",
    }


@app.get(
    "/echo",
    summary="Echo Client Headers",
    description="受信した HTTP ヘッダをクライアントに返却します。",
    response_model=EchoResponse,
)
def echo(request: Request):
    headers = dict(request.headers)
    return {"headers": headers}
