from fastapi import APIRouter, Depends, HTTPException
from users.models import User
from .models import Bookmark, BookmarkPatchModel, Folder
from bookmarker.generic_response import SuccessResponse
from users.helpers import authorization
from typing import List

router = APIRouter()

RequestBookmark = Bookmark.get_pydantic(exclude={"user", "id", "folder"})
ResponseBookmark = Bookmark.get_pydantic(exclude={"user", "folder"})
ResponseBookmarkUserId = Bookmark.get_pydantic(include={"id", "title", "url", "favicon_url",  "user__id"})

@router.post("/bookmark/create/", response_model=ResponseBookmark)
async def create_bookmark(bookmark: RequestBookmark, user: User = Depends(authorization)):
    return await Bookmark(user=user, **bookmark.dict()).save()

@router.get("/bookmarks", response_model=List[ResponseBookmark])
async def get_user_bookmarks(user: User = Depends(authorization)):
    return await user.bookmarks.filter(folder__isnull=True).all()

@router.get("/bookmark/{id}", response_model=ResponseBookmarkUserId)
async def get_bookmark(id: int, user: User = Depends(authorization)):
    bookmark = await Bookmark.objects.get_or_none(id=id)
    if bookmark:
        if user.id == bookmark.user.id:
            return bookmark
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Bookmark not found")

@router.put("/bookmark/{id}/", response_model=ResponseBookmarkUserId)
async def edit_bookmark(id: int, bookmark: RequestBookmark, user: User = Depends(authorization)):
    db_bookmark = await Bookmark.objects.get_or_none(id=id)
    if db_bookmark:
        if user.id == db_bookmark.user.id:
            return await db_bookmark.update(**bookmark.dict())
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Bookmark not found")

@router.patch("/bookmark/{id}/", response_model=ResponseBookmarkUserId)
async def update_bookmark(id: int, bookmark: BookmarkPatchModel, user: User = Depends(authorization)):
    db_bookmark = await Bookmark.objects.get_or_none(id=id)
    if db_bookmark:
        if user.id == db_bookmark.user.id:
            update_data = bookmark.dict(exclude_unset=True)
            return await db_bookmark.update(**update_data)
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Bookmark not found")

@router.delete("/bookmark/{id}/", response_model=SuccessResponse)
async def delete_bookmark(id: int, user: User = Depends(authorization)):
    db_bookmark = await Bookmark.objects.get_or_none(id=id)
    if db_bookmark:
        if user.id == db_bookmark.user.id:
            await db_bookmark.delete()
            return SuccessResponse(detail="Bookmark successfully deleted")
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Bookmark not found")
