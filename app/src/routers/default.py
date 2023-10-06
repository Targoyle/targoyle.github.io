from typing import Dict

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()


class HelloWorldResponse(BaseModel):
    Hello: str


class EchoResponse(BaseModel):
    headers: Dict[str, str]


@router.get(
    "/",
    summary="Hello World Endpoint",
    description="このエンドポイントは、簡単な 'Hello, World!' メッセージを返却します。",
    response_model=HelloWorldResponse,
)
def hello_world():
    return {
        "Hello": "World",
    }


@router.get(
    "/echo",
    summary="Echo Client Headers",
    description="受信した HTTP ヘッダをクライアントに返却します。",
    response_model=EchoResponse,
)
def echo(request: Request):
    headers = dict(request.headers)
    headers.pop("host", None)
    return {"headers": headers}
