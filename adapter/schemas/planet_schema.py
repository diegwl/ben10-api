from tortoise.models import Model
from tortoise import fields

class PlanetModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    # species = fields.ReverseRelation()