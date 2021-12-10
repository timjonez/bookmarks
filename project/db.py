import databases
import ormar
import sqlalchemy

database = databases.Database("sqlite:///project/db.sqlite")
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
