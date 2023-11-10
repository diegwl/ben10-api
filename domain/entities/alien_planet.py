from pydantic import Field, BaseModel
from domain.entities.planet import Planet

class AlienPlanetDto(BaseModel):
    name: str
    species: str
    home_world: Planet
    body: str
    
class AlienPlanet(AlienPlanetDto):
    id: int