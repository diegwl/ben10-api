from pydantic import BaseModel
from adapter.alien_adapter import AlienTortoiseAdapter
from domain.entities.alien import AlienDto
from domain.entities.alien_planet import AlienPlanetDto

class AlienService(BaseModel):
    
    adapter: AlienTortoiseAdapter
    
    async def list(self):
        return await self.adapter.list()
    
    async def create(self, alien: AlienDto):
        return await self.adapter.create(alien)
    
    async def get(self, alien_id: int):
        return await self.adapter.get(alien_id)
    
    async def put(self, alien: AlienDto, alien_id: int):
        return await self.adapter.put(alien, alien_id)
    
    async def delete(self, alien_id: int):
        return await self.adapter.delete(alien_id)
    
    async def search(self, alien_name: str, in_lucky: bool):
        return await self.adapter.search(alien_name, in_lucky)