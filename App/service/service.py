import requests
import json

from models.models import Pirate

def buscar_dados_kanye():
    request = requests.get("https://api.kanye.rest/")
    content = json.loads(request.content)
    return content['quote']

def buscar_dados_onepiece_local():
    request = requests.get("http://10.234.91.70:8000/characters/")
    content = json.loads(request.content)
    return content

def buscar_pirata(id: int):
    request = requests.get(f"http://10.234.91.70:8000/characters/{id}/")
    content = json.loads(request.content)
    return content

# def criar_pirata(pirate: Pirate):
#     request = requests.post(f"http://10.234.91.70:8000/characters/", data=pirate)
#     content = json.loads(request.content)
#     return content