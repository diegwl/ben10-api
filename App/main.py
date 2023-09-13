from typing import Optional

from fastapi import FastAPI, HTTPException, status, Response, Path

from models import Alien, aliens

from busca_api import buscar_dados

app = FastAPI(
    root_path="api/v1/aliens",
)

# aliens = {
#     1: {
#         "name": "Wildmutt",
#         "species": "Vulpimancer",
#         "homeWorld": "Vulpin",
#         "body": "Animalistic"
#     },
#     2: {
#         "name": "Heatblast",
#         "species": "Pyronita",
#         "homeWorld": "Pyros",
#         "body": "Fiery Humanoid"
#     },
#     3: {
#         "name": "Diamondhead",
#         "species": "Petrosapien",
#         "homeWorld": "Petropia",
#         "body": "Crystalline Humanoid"
#     },
#     4: {
#         "name": "XLR8",
#         "species": "Kineceleran",
#         "homeWorld": "Kinet",
#         "body": "Humanoid Velociraptor"
#     },
#     5: {
#         "name": "Grey Matter",
#         "species": "Galvan",
#         "homeWorld": "Galvan Prime",
#         "body": "Humanoid Frog"
#     },
#     6: {
#         "name": "Four Arms",
#         "species": "Tetramand",
#         "homeWorld": "Khoros",
#         "body": "Four-Armed Humanoid"
#     },
#     7: {
#         "name": "Stinkfly",
#         "species": "Lepidopterran",
#         "homeWorld": "Lepidopterra",
#         "body": "Winged Insectoid"
#     },
#     8: {
#         "name": "Ripjaws",
#         "species": "Piscciss Volann",
#         "homeWorld": "Piscciss",
#         "body": "Humanoid Anglerfish"
#     },
#     9: {
#         "name": "Upgrade",
#         "species": "Galvanic Mechamorph",
#         "homeWorld": "Galvan B",
#         "body": "Technological Humanoid"
#     },
#     10: {
#         "name": "Ghostfreak",
#         "species": "Ectonurite",
#         "homeWorld": "Anur Phaetos",
#         "body": "Ghost"
#     },
# }

@app.get('/api/v1/aliens')
async def get_aliens():
    return aliens

@app.get('/api/v1/aliens/{alien_id}')
async def get_alien(alien_id:int = Path(title='ID do Alien')):
    try:
        alien = aliens[alien_id-1]
        alien.id = alien_id
        return alien
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alien não encontrado')

@app.post('/api/v1/aliens', status_code=status.HTTP_201_CREATED)
async def post_alien(alien: Alien):
    next_id: int = len(aliens) + 1
    alien.id = next_id
    aliens.append(alien)
    return alien

@app.put('/api/v1/aliens/{alien_id}')
async def put_alien(alien_id: int, alien: Alien):
    if alien_id <= len(aliens):
        alien.id = alien_id
        aliens[alien_id-1] = alien
        return alien
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse alien não existe.")

@app.delete('/api/v1/aliens/{alien_id}')
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

@app.get('/api/v1/kanye')
async def kanye():
    quote = buscar_dados()
    return {"Kanye said": quote}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host='10.234.88.203', port=8000, log_level="info", reload=True)
