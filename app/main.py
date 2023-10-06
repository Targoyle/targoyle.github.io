from typing import Dict

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://targoyle.github.io"],
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

    excluded_headers = [
        "x-vercel-proxy-signature",
        "x-vercel-proxy-signature-ts",
        "x-vercel-id",
        "x-vercel-deployment-url",
        "forwarded",
    ]

    for header in excluded_headers:
        headers.pop(header, None)

    return {"headers": headers}
