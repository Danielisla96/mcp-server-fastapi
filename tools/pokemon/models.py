from pydantic import BaseModel
from typing import List


class PokemonInfo(BaseModel):
    id: int
    name: str
    weight: int
    types: List[str]