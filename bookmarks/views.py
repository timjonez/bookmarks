from fastapi import HTTPException, APIRouter, Request, Depends
from users.models import Users
from users.views import ResponseUser
from .models import Bookmarks
from typing import List
from users.helpers import is_authorized

router = APIRouter()

RequestBookmark = Bookmarks.get_pydantic(exclude={"id","user"})
ResponseBookmark = Bookmarks.get_pydantic(exclude={"user__password"})

@router.post("/bookmark/create", response_model=ResponseBookmark)
async def create_user(bookmark: RequestBookmark, user_data: dict = Depends(is_authorized)):
    user = await Users.objects.get_or_none(email=user_data)
    dict_bookmark = bookmark.dict()
    dict_bookmark['user'] = user
    new_bookmark = await Bookmarks.objects.create(**dict_bookmark)
    user = await Users.objects.get_or_none(email=user_data)
    return new_bookmark

@router.get("/bookmarks")
async def get_bookmarks(user_data: dict = Depends(is_authorized)):
    user = await Users.objects.get_or_none(email="timjonez@protonmail.com")
    return await user.bookmarks.all()
