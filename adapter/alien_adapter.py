from typing import TypeVar
from pydantic import BaseModel
from domain.entities.alien import AlienDto
from adapter.schemas.planet_schema import PlanetModel

DataT = TypeVar("DataT")

class AlienTortoiseAdapter(BaseModel):
    
    model: DataT
    
    async def list(self):
        return await self.model.all()
    
    async def create(self, alien: AlienDto):
        planet = await PlanetModel.get(id=alien.home_world)
        alien.home_world = planet
        return await self.model.create(**alien.model_dump())
    
    async def get(self, alien_id: int):
        return await self.model.get(id=alien_id)
    
    async def put(self, alien: AlienDto, alien_id: int):
        return await self.model.filter(id=alien_id).update(**alien.model_dump())
    
    async def delete(self, alien_id: int):
        return await self.model.filter(id=alien_id).delete()