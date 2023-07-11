from pydantic import BaseModel
from typing import Optional

class StudioIn(BaseModel):
    name: str


class StudioOut(StudioIn):
    id: int


class StudioUpdate(StudioIn):
    name: Optional[str] = None
