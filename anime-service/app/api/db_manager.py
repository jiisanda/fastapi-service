from app.api.models import AnimeIn, AnimeOut, AnimeUpdate
from app.api.db import anime, database

async def add_anime(payload: AnimeIn):
    query = anime.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_anime():
    query = anime.select()

    return await database.fetch_all(query=query)


async def get_anime(id):
    query = anime.select(anime.c.id == id)

    return await database.fetch_one(query=query)


async def delete_anime(id: int):
    query = anime.delete().where(anime.c.id==id)

    return await database.execute(query=query)


async def update_anime(id:int, payload:AnimeIn):
    query = (
        anime
        .update()
        .where(movies.c.id==id)
        .values(**payload.dict())
    )

    return await database.execute(query=query)
