from pydantic import BaseModel
from typing import List, Optional


class AnimeIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    characters: List[str]
    studio_id: List[int]


class AnimeOut(AnimeIn):
    id: int


class AnimeUpdate(AnimeIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    characters: Optional[List[str]] = None
    studio_id: Optional[List[int]] = None
