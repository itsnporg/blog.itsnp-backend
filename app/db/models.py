import peewee as models
from .config import db


class BaseModel(models.Model):
    """A base model that will use our database."""
    class Meta:
        database = db
