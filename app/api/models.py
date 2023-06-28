from pydantic import BaseModel
from typing import List


class Anime(BaseModel):
    name: str
    plot: str
    genres: List[str]
    characters: List[str]
    studio: List[str]