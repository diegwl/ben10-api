from fastapi import APIRouter, FastAPI, HTTPException, status, Response, Path, Query

from service.service import buscar_dados_kanye

router = APIRouter()

# CONSUMINDO API KANYE
@router.get('')
async def kanye():
    quote = buscar_dados_kanye()
    return {"Kanye said": quote}