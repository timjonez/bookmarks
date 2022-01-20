import ormar
from bookmarker.db import BaseMeta
from users.models import User

class Folder(ormar.Model):
    class Meta(BaseMeta):
        tablename = "folders"

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=128)
    user: User = ormar.ForeignKey(User, nullable=False)
