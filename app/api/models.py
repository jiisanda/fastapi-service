from pydantic import BaseModel
from typing import List


class AnimeIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    characters: List[str]
    status: List[str]


class AnimeOut(AnimeIn):
    id: int


class AnimeOut(AnimeIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    characters: Optional[List[str]] = None
    status: Optional[List[str]] = None
