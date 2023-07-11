from fastapi import HTTPException, APIRouter
from typing import List

from app.api.models import AnimeIn, AnimeOut
from app.api import db_manager
from app.api.service import is_studio_present

anime = APIRouter()


@anime.get('/', response_model=List[AnimeOut])
async def index():
    return await db_manager.get_all_anime()

@anime.post('/', status_code=201)
async def add_anime(payload: AnimeIn):
    for studio in payload.studio_id:
        if not is_studio_present(studio_id):
            raise HTTPException(status_code=404, detail=f"Studio with id:{studio_id} not found...")

    anime_id = await db_manager.add_anime(payload)
    response = {
        "id": anime_id,
        **payload.dict()
    }

    return response

@anime.put('/{id}')
async def update_anime(id: int, payload: AnimeIn):
    anime = await db_manager.get_anime(id)
    if not anime:
        raise HTTPException(status_code=404, detail=f"Anime with {id} not found.")
    
    update_data = payload.dict(exclude_unset=True)
    
    if 'studio_id' in update_data:
        for studio_id in payload.studio_id:
            if not is_studio_present(studio_id):
                raise HTTPException(status_code=404, detail=f"Anime with given id: {studio_id} not found...")

    anime_in_db = AnimeIn(**anime)

    updated_anime = anime_in_db.copy(update=update_data)

    return await db_manager.update_movie(id, updated_anime)


@anime.delete('/{id}')
async def delete_anime(id: int):
    anime = await db_manager.get_anime(id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime with the given ID not found!")
    return await db_manager.delete_anime(id)
