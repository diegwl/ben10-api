from fastapi import FastAPI

from port.fastapi.configuration import configure_routers, configure_tortoise

def create_application():
    application = FastAPI(
        title="Ben 10 API"
    )
    
    configure_routers(application)
    configure_tortoise(application)
    
    return application

core_module = create_application()