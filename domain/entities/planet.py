from pydantic import Field, BaseModel
from typing import List
from domain.entities.alien import Alien

class PlanetDto(BaseModel):
    name: str
    
class Planet(PlanetDto):
    id: int
    
class PlanetDetail(Planet):
    species: List[Alien]