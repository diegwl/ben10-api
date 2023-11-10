from typing import TypeVar
from pydantic import BaseModel
from domain.entities.planet import PlanetDto

DataT = TypeVar("DataT")

class PlanetTortoiseAdapter(BaseModel):
    
    model: DataT
    
    async def list(self):
        return await self.model.all()
    
    async def create(self, planet: PlanetDto):
        return await self.model.create(**planet.model_dump())
    
    async def get(self, planet_id: int):
        return await self.model.get(id=planet_id)
    
    async def put(self, planet: PlanetDto, planet_id: int):
        return await self.model.filter(id=planet_id).update(**planet.model_dump())
    
    async def delete(self, planet_id: int):
        return await self.model.filter(id=planet_id).delete()