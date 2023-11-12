from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from domain.entities.planet import Planet, PlanetDto, PlanetDetail
from domain.service.planet_service import PlanetService

from port.factory.planet_factory import planet_factory

router = APIRouter(
    prefix='/planets',
    tags=["planets"]
)

@router.get("/", response_model=List[Planet])
async def list_planets(service: PlanetService = Depends(planet_factory)):
    return await service.list()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Planet)
async def create_planet(body: PlanetDto, service: PlanetService = Depends(planet_factory)):
    try:
        planet = PlanetDto(**body.model_dump())
        return await service.create(planet)
    except:
        raise HTTPException(detail='Home World não existente.', status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/{planet_id}", status_code=status.HTTP_200_OK, response_model=PlanetDetail)
async def get_planet(planet_id: int, service: PlanetService = Depends(planet_factory)):
    try:
        return await service.get(planet_id)
    except:
        raise HTTPException(detail='Planet não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
    
@router.put("/{planet_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_planet(planet_id: int, planet: PlanetDto, service: PlanetService = Depends(planet_factory)):
    return await service.put(planet, planet_id)

@router.delete("/{planet_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_planet(planet_id: int, service: PlanetService = Depends(planet_factory)):
    return await service.delete(planet_id)