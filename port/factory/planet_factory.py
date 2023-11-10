from adapter.planet_adapter import PlanetTortoiseAdapter
from adapter.schemas.planet_schema import PlanetModel
from domain.service.planet_service import PlanetService

def planet_factory():
    adapter = PlanetTortoiseAdapter(model=PlanetModel)
    service = PlanetService(adapter=adapter)
    return service