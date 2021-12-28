from fastapi import FastAPI
import uvicorn
import bookmarker

from bookmarker.db import database
from users.views import router as user_router
from bookmarks.views import router as bookmark_router


app = FastAPI()

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

app.include_router(user_router)
app.include_router(bookmark_router)


@app.get('/')
async def home():
    return {"message": "this is a test"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
