from fastapi import APIRouter, FastAPI, HTTPException, status, Response, Path, Query

from models.models import Alien, aliens

router = APIRouter()

# API - BEN 10
@router.get('')
async def get_aliens():
    return aliens

@router.get('/{alien_id}')
async def get_alien(alien_id:int = Path(title='ID do Alien')):
    try:
        alien = aliens[alien_id-1]
        alien.id = alien_id
        return alien
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alien não encontrado')

@router.post('', status_code=status.HTTP_201_CREATED)
async def post_alien(alien: Alien):
    next_id: int = len(aliens) + 1
    alien.id = next_id
    aliens.append(alien)
    return alien

@router.put('/{alien_id}')
async def put_alien(alien_id: int, alien: Alien):
    if alien_id <= len(aliens):
        alien.id = alien_id
        aliens[alien_id-1] = alien
        return alien
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse alien não existe.")

@router.delete('/{alien_id}')
async def delete_alien(alien_id: int):
    if alien_id <= len(aliens):
        del aliens[alien_id-1]
        cont = 1
        for alien in aliens:
            alien.id = cont
            cont += 1
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse alien não existe.")