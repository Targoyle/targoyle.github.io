import base64
from io import BytesIO
from typing import Dict

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

FAVICON_BASE64 = "R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAAAICTAEAOw=="

router = APIRouter()


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


@router.get(
    "/",
    summary="Hello World Endpoint",
    description="このエンドポイントは、'Hello, World!' を返却します。",
    response_model=HelloWorldResponse,
)
def hello_world():
    return {
        "Hello": "World",
    }


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return StreamingResponse(
        BytesIO(base64.b64decode(FAVICON_BASE64)), media_type="image/x-icon"
    )


@router.get(
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


@router.get(
    "/location",
    summary="Get client location",
    description="受信した HTTP ヘッダ, IP アドレスを元に、クライアントの位置情報を返却します。",
    response_model=LocationResponse,
)
def location(request: Request):
    headers = dict(request.headers)

    ip = headers.get("x-forwarded-for") or headers.get("x-vercel-proxied-for")
    latitude = headers.get("x-vercel-ip-latitude")
    longitude = headers.get("x-vercel-ip-longitude")
    country = headers.get("x-vercel-ip-country")
    timezone = headers.get("x-vercel-ip-timezone")

    try:
        city = headers.get("x-vercel-ip-city")
    except Exception as e:
        city = "-"

    return {
        "ip": ip,
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "country": country,
        "timezone": timezone,
    }
