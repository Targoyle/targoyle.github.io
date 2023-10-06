from fastapi import FastAPI

from routers import default

app = FastAPI()

app.include_router(default.router)
