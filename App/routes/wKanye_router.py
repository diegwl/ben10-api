from fastapi import APIRouter, FastAPI, HTTPException, status, Response, Path, Query
import random

from models.models import Alien, aliens
from service.service import buscar_dados_kanye

router = APIRouter()

@router.get('/{alien_id}')
async def get_alien(alien_id: int = Path(title='ID do Alien')):
    try:
        alien = aliens[alien_id-1]
        quote = buscar_dados_kanye()
        return {"What would Kanye say to the "+ alien.name +"if he saw him?": quote}

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alien não encontrado')

