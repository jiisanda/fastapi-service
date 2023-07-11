from fastapi import APIRouter, HTTPException

from app.api import db_manager
from app.api.models import StudioIn, StudioOut, StudioUpdate

studio = APIRouter()


@studio.post('/', response_model=StudioOut, status_code=201)
async def create_studio(payload: StudioIn):
    studio_id = await db_manager.add_studio(payload)
    
    response = {
        'id': studio_id,
        **payload.dict()
    }
    
    return response


@studio.get('/{id}/', response_model=StudioOut)
async def get_studio(id: int):
    studio = await db_manager.get_studio(id)
    if not studio:
        raise HTTPException(status_code=404, detail="Studio not found!")
    return studio
