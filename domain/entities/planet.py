from pydantic import Field, BaseModel
from typing import List, Optional
from domain.entities.alien import Alien

class PlanetDto(BaseModel):
    name: str
    
class Planet(PlanetDto):
    id: int
    
class PlanetDetail(Planet):
    aliens: Optional[List[Alien]]