from fastapi import APIRouter, FastAPI, HTTPException, status, Response, Path, Query

from service.service import buscar_dados_onepiece_local, buscar_pirata

router = APIRouter()

# CONSUMINDO API REDE LOCAL
@router.get('/')
async def onepiece():
    data = buscar_dados_onepiece_local()
    return data

@router.get('/{pirate_id}')
async def pirate():
    data = buscar_pirata()
    return data