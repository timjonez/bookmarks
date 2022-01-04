# Bookmarker
## FastAPI + Ormar + Alembic
```
#Install dependencies in virtual environment 
pipenv install

#Initialize database with migrations
alembic upgrade head

#Run app
uvicorn bookmarker.main:app --reload

#Create migration
alembic revision --autogenerate -m "message"
```
