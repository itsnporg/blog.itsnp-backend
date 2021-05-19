import peewee as models
from app.db.config import db
import datetime

class BaseModel(models.Model):
    """A base model that will use our database."""
    class Meta:
        database = db


class User(BaseModel):
    email = models.CharField(unique=True)
    hashed_password = models.CharField()
    is_active = models.BooleanField(default=True)


class Blog(BaseModel):
    title = models.CharField(max_length=20)
    user = models.ForeignKeyField(User, backref='blogs')
    body = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    is_published = models.BooleanField(default=False)
