import os
from fastapi import FastAPI
from port.fastapi.router import alien_router, planet_router
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv

load_dotenv()

def configure_routers(application: FastAPI):
    application.include_router(alien_router.router, prefix='/api/v1')
    application.include_router(planet_router.router, prefix='/api/v1')
    
def configure_tortoise(application: FastAPI):
    register_tortoise(
        application,
        generate_schemas=True,
        db_url=os.environ.get("DATABASE_URL"),
        modules={
            "models": [
                "adapter.schemas.alien_schema",
                "adapter.schemas.planet_schema"
            ],
        }
    )