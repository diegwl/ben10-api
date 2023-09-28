from fastapi import APIRouter, FastAPI, HTTPException, status, Response, Path, Query

from service.service import buscar_dados_onepiece_local, buscar_pirata

from models.models import Pirate

router = APIRouter()

# CONSUMINDO API REDE LOCAL
@router.get('/')
async def onepiece():
    try:
        data = buscar_dados_onepiece_local()
        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Piratas não encontrados')
        return data
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Piratas não encontrados')


@router.get('')
async def get_pirate(pirate_id: int):
    try:
        data = buscar_pirata(pirate_id)
        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pirata não encontrado')
        return data
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pirata não encontrado')

# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def post_pirate(pirate: Pirate):
#     try:
#         data = criar_pirata(pirate)
#         return data
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pirata não criado')