from pydantic import BaseModel
from adapter.planet_adapter import PlanetTortoiseAdapter
from domain.entities.planet import PlanetDto
from adapter.schemas.alien_schema import AlienModel

class PlanetService(BaseModel):
    
    adapter: PlanetTortoiseAdapter
    
    async def list(self):
        return await self.adapter.list()
    
    async def create(self, planet: PlanetDto):
        return await self.adapter.create(planet)
    
    async def get(self, planet_id: int):
        planet = await self.adapter.get(planet_id)
        planet.aliens = await AlienModel.filter(home_world_id=planet.id)
        return planet
    
    async def put(self, planet: PlanetDto, planet_id: int):
        return await self.adapter.put(planet, planet_id)
    
    async def delete(self, planet_id: int):
        return await self.adapter.delete(planet_id)