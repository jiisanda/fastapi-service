from app.api.models import StudioIn, StudioOut, StudioUpdate
from app.api.db import studio, database

async def add_studio(payload: StudioIn):
    query = studio.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_studio(id):
    query = studio.select(studio.c.id==id)

    return await database.fetch_one(query=query)