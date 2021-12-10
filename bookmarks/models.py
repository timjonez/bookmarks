import ormar
import datetime
import sqlalchemy
from project.db import BaseMeta
from users.models import Users


class Bookmarks(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bookmarks"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    title: str = ormar.String(max_length=128)
    url: str = ormar.String(max_length=254)
    user: Users = ormar.ForeignKey(Users)
