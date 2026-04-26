from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from dotenv import load_dotenv
import os
from app.api.routes import router

app = FastAPI(title="Spotify V4")

load_dotenv()

app.add_middleware(
    SessionMiddleware,
    secret_key="SECRET_KEY"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "DAMIAN SPOTIFY V4 TEST"
    }