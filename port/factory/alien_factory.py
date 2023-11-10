from adapter.alien_adapter import AlienTortoiseAdapter
from adapter.schemas.alien_schema import AlienModel
from domain.service.alien_service import AlienService

def alien_factory():
    adapter = AlienTortoiseAdapter(model=AlienModel)
    service = AlienService(adapter=adapter)
    return service