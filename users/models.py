import pyjwt
import bcrypt
import ormar
import datetime
import sqlalchemy
from bookmarker.db import BaseMeta
from bookmarker.settings import settings


class Users(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    email: str = ormar.String(max_length=64, unique=True)
    password: str = ormar.String(max_length=128)
    is_active: bool = ormar.Boolean(default=True)
    is_admin: bool = ormar.Boolean(default=False)
    joined_date: datetime.datetime = ormar.DateTime(server_default=sqlalchemy.func.now())

    def password_is_valid(self, password):
        if bcrypt.checkpw(password, self.password):
            return True
        return False

    def login(self, password):
        if self.password_is_valid(password):
            return pyjwt.encode(self.email, settings.secret_key)
        return None
