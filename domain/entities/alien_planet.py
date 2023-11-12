from pydantic import Field, BaseModel
from adapter.schemas.planet_schema import PlanetModel
from domain.entities.planet import Planet
from typing import Optional, List


class AlienPlanetDto(BaseModel):
    name: str
    species: str
    home_world_id: int
    body: str
    
class AlienPlanet(AlienPlanetDto):
    id: int
    home_world: Planet