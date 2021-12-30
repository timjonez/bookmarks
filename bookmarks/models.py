import ormar
from bookmarker.db import BaseMeta
from users.models import User
from pydantic import BaseModel
from typing import Optional


class Bookmark(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bookmarks"
    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    title: str = ormar.String(max_length=128)
    url: str = ormar.String(max_length=254)
    user: User = ormar.ForeignKey(User, nullable=False)


class BookmarkPatchModel(BaseModel):
    title: Optional[str]
    url: Optional[str]
