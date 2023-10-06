from fastapi import FastAPI

from routers import default

app = FastAPI(
    openapi_url="/openapi.json",  # "/openapi.json" or None
    docs_url="/docs",  # "/docs" or None
    redoc_url="/redoc",  # "/redoc" or None
)

app.include_router(default.router)

'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World src"}
'''
