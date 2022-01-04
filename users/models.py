import jwt
import bcrypt
import ormar
import validators
import sqlalchemy
from bookmarker.db import BaseMeta
from bookmarker.settings import settings, password_validator
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, validator


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    email: str = ormar.String(max_length=64, unique=True)
    password: str = ormar.String(max_length=128)
    is_active: bool = ormar.Boolean(default=True)
    is_admin: bool = ormar.Boolean(default=False)
    joined_date: datetime = ormar.DateTime(server_default=sqlalchemy.func.now())

    async def save(self, *args, **kwargs):
        self.password = await self.hash_password(self.password)
        return await super().save(*args, **kwargs)

    async def password_is_valid(self, password):
        return bcrypt.checkpw(password.encode(), self.password.encode())

    async def login(self, password):
        if await self.password_is_valid(password):
            expire_date = datetime.now(tz=timezone.utc) + timedelta(hours=3)
            return jwt.encode({"email": self.email, "exp": expire_date}, settings.secret_key, algorithm="HS256")
        return None

    async def hash_password(self, raw_password):
        return bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt(rounds=settings.salt_rounds))


class BaseUserModel(BaseModel):
    email: str

    @validator('email')
    def email_is_valid(cls, value):
        if validators.email(value):
            return value
        raise ValueError("Email must be a valid email address")

class UserWriteModel(BaseUserModel):
    password: str

    @validator('password')
    def password_is_valid(cls, value):
        if password_validator.validate(value):
            return value
        raise ValueError("Password is not valid")

class UserReadModel(BaseUserModel):
    id: int
    is_active: bool
    is_admin: bool
    joined_date: datetime
    bookmarks: list

class LoginSchema(BaseModel):
    token: str
