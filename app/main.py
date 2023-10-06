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
    allow_origins=[
        "https://targoyle.github.io",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HelloWorldResponse(BaseModel):
    Hello: str = "World"


class EchoResponse(BaseModel):
    headers: Dict[str, str]


class LocationResponse(BaseModel):
    ip: str = "192.0.2.0"
    latitude: str = "35.6768"
    longitude: str = "139.7522"
    city: str = "Tokyo"
    country: str = "JP"
    timezone: str = "Asia/Tokyo"


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


@app.get(
    "/location",
    summary="Get client location",
    description="受信したHTTPヘッダーを基に、クライアントの位置情報を返却します。",
    response_model=LocationResponse,
)
def location(request: Request):
    headers = dict(request.headers)

    ip = headers.get("x-forwarded-for") or headers.get("x-vercel-proxied-for")
    latitude = headers.get("x-vercel-ip-latitude")
    longitude = headers.get("x-vercel-ip-longitude")
    city = headers.get("x-vercel-ip-city")
    country = headers.get("x-vercel-ip-country")
    timezone = headers.get("x-vercel-ip-timezone")

    return {
        "ip": ip,
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "country": country,
        "timezone": timezone,
    }
