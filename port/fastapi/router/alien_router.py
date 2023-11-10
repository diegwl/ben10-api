from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from domain.entities.alien import Alien, AlienDto
from domain.service.alien_service import AlienService

from port.factory.alien_factory import alien_factory

router = APIRouter(
    prefix='/aliens',
    tags=["aliens"]
)

@router.get("/", response_model=List[Alien])
async def list_aliens(service: AlienService = Depends(alien_factory)):
    return await service.list()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Alien)
async def create_alien(body: AlienDto, service: AlienService = Depends(alien_factory)):
    alien = AlienDto(**body.model_dump())
    return await service.create(alien)

@router.get("/{alien_id}", status_code=status.HTTP_200_OK, response_model=Alien)
async def get_alien(alien_id: int, service: AlienService = Depends(alien_factory)):
    try: 
        return await service.get(alien_id)
    except:
        raise HTTPException(detail='Alien não encontrado.', status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{alien_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_alien(alien_id: int, alien: AlienDto, service: AlienService = Depends(alien_factory)):
    return await service.put(alien, alien_id)

@router.delete("/{alien_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_alien(alien_id: int, service: AlienService = Depends(alien_factory)):
    return await service.delete(alien_id)