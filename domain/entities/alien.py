from pydantic import Field, BaseModel
from typing import Optional

class AlienDto(BaseModel):
    name: str
    species: str
    home_world_id: int
    body: str
    
class Alien(AlienDto):
    id: int