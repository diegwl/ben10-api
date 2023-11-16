from typing import TypeVar
from pydantic import BaseModel
from domain.entities.alien import AlienDto
from domain.entities.alien_planet import AlienPlanetDto
from adapter.schemas.planet_schema import PlanetModel

DataT = TypeVar("DataT")

class AlienTortoiseAdapter(BaseModel):
    
    model: DataT
    
    async def list(self):
        return await self.model.all()
    
    async def create(self, alien: AlienDto):
        # planet = await PlanetModel.get(id=alien.home_world)
        # alien.home_world = planet
        return await self.model.create(**alien.model_dump())
    
    async def get(self, alien_id: int):
        alien = await self.model.get_or_none(id=alien_id)
        if alien:
            alien.home_world = await PlanetModel.get(id=alien.home_world_id)
        return alien
    
    async def put(self, alien: AlienDto, alien_id: int):
        return await self.model.filter(id=alien_id).update(**alien.model_dump())
    
    async def delete(self, alien_id: int):
        return await self.model.filter(id=alien_id).delete()
    
    async def search(self, alien_name: str, in_lucky: bool):
        if in_lucky:
            return await self.model.filter(name__icontains=alien_name).get_or_none().first()
        else:
            return await self.model.filter(name__icontains=alien_name).all()