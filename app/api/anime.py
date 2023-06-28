from fastapi import HTTPException, APIRouter
from typing import List

from app.api.models import Anime

anime = APIRouter()

anime_db = [
    {
        'name': '進撃の巨人',
        'plot': 'Eren Yeager is a boy who lives in the town of Shiganshina, located on the outermost of three circular walls which protect their inhabitants from Titans.', 
        'genres': ['Action', 'Dark-Fantasy', 'Post-apocalyptic'],
        'characters': ['Eren Yeager', 'Mikasa Ackerman', ' Armin Arlert', 'Levi', 'Hange Zoe'],
        'studio': ['Wit Studio', 'MAPPA'], 
    }
]


@anime.get('/', response_model=List[Anime])
async def index():
    return anime_db

@anime.post('/', status_code=201)
async def add_anime(payload: Anime):
    anime = payload.dict()
    anime_db.append(anime)
    return {'id': len(anime_db) - 1}

@anime.put('/{id}')
async def update_anime(id: int, payload: Anime):
    anime = payload.dict()
    anime_length = len(anime_db)
    if 0 <= id <= anime_length:
        anime_db[id] = anime
        return anime
    raise HTTPException(status_code=404, detail="Anime with the given ID not found!")

@anime.delete('/{id}')
async def delete_anime(id: int):
    anime_length = len(anime_db)
    if 0 <= id <= anime_length:
        del anime_db[id]
        return None
    raise HTTPException(status_code=404, detail="Anime with the given ID not found!")