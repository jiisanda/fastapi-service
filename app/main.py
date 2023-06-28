from fastapi import FastAPI

from app.api.anime import anime

app = FastAPI()

app.include_router(anime)