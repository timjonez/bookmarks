from fastapi import APIRouter, Depends
from users.models import User
from .models import Bookmark
from users.helpers import is_authorized
from typing import List

router = APIRouter()

RequestBookmark = Bookmark.get_pydantic(exclude={"user"})

@router.post("/bookmark/create", response_model=RequestBookmark)
async def create_bookmark(bookmark: RequestBookmark, user_email: str = Depends(is_authorized)):
    user = await User.objects.get(email=user_email)
    return await Bookmark(user=user, **bookmark.dict()).save()

@router.get("/bookmarks", response_model=List[RequestBookmark])
async def get_user_bookmarks(user_email: str = Depends(is_authorized)):
    user = await User.objects.get(email=user_email)
    return await user.bookmarks.all()
