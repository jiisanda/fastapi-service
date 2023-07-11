from fastapi import FastAPI

from app.api.studio import studio
from app.api.db import database, metadata, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(studio, prefix='/api/v1/studio', tags=['Studio'])
