import ormar
from bookmarker.db import BaseMeta
from users.models import User
from pydantic import BaseModel, HttpUrl, validator
import validators
from typing import Optional


class Bookmark(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bookmarks"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    title: str = ormar.String(max_length=128)
    url: HttpUrl = ormar.String(max_length=254)
    favicon_url: HttpUrl = ormar.String(max_length=254, nullable=True)
    user: User = ormar.ForeignKey(User, nullable=False)

    async def save(self, *args, **kwargs):
        if self.favicon_url is None:
            self.favicon_url = f"{self.url}/favicon.ico"
        return await super().save(*args, **kwargs)

    @validator('url')
    def url_is_valid(cls, value):
        if validators.url(value):
            return value
        raise ValueError("Url must be a valid url")

    @validator('favicon_url')
    def favicon_is_valid(cls, value):
        if value is None:
            return value
        elif validators.url(value):
            return value
        raise ValueError("Favicon url must be a valid url")


class BookmarkPatchModel(BaseModel):
    title: Optional[str]
    url: Optional[str]
