import requests
import json

def buscar_dados():
    request = requests.get("https://api.kanye.rest/")
    content = json.loads(request.content)
    return content['quote']