from fastapi import FastAPI
import uvicorn

from bookmarker.db import database
from users.views import router as user_router
from bookmarks.views import router as bookmark_router
from folders.views import router as folder_router
from .settings import pub_settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(**pub_settings.dict())

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(folder_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
