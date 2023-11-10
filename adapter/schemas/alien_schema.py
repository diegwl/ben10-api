from tortoise.models import Model
from tortoise import fields
from adapter.schemas.planet_schema import PlanetModel

class AlienModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    species = fields.TextField()
    home_world = fields.ForeignKeyField('models.PlanetModel', related_name='planets')
    body = fields.TextField()