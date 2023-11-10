from tortoise.models import Model
from tortoise import fields

class AlienModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    species = fields.TextField()
    home_world = fields.TextField()
    body = fields.TextField()