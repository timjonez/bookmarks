import ormar
import datetime
import sqlalchemy
from bookmarker.db import BaseMeta


class Users(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    email: str = ormar.String(max_length=64, unique=True)
    password: str = ormar.String(max_length=128)
    is_active: bool = ormar.Boolean(default=True)
    is_admin: bool = ormar.Boolean(default=False)
    joined_date: datetime.datetime = ormar.DateTime(server_default=sqlalchemy.func.now())
