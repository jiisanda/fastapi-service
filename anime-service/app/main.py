from fastapi import FastAPI

from app.api.anime import anime
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    return await database.connect()


@app.on_event("shutdown")
async def shutdown():
    return await database.disconnect()


app.include_router(anime, prefix='/api/v1/anime', tags=['anime'])
