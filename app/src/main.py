"""
from fastapi import FastAPI

from routers import default

app = FastAPI()

app.include_router(default.router)
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}
