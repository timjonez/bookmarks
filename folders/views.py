from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bookmarker.generic_response import SuccessResponse
from users.helpers import authorization
from bookmarks.models import Bookmark
from users.models import User
from .models import Folder

router = APIRouter()

RequestFolder = Folder.get_pydantic(include={"name", "bookmarks"}, exclude={"bookmarks__user"})
ResponseFolder = Folder.get_pydantic(exclude={"user", "bookmarks__user"})
PatchFolder = Folder.get_pydantic(include={"name"})

@router.post("/folder/create/", response_model=ResponseFolder)
async def create_folder(folder: RequestFolder, user: User = Depends(authorization)):
    return await Folder(user=user, **folder.dict()).save()

@router.get("/folders", response_model=List[ResponseFolder])
async def get_user_folders(user: User = Depends(authorization)):
    return await user.folders.all()

@router.get("/folder/{id}", response_model=ResponseFolder)
async def get_folder(id: int, user: User = Depends(authorization)):
    folder = await Folder.objects.select_related("bookmarks").get_or_none(id=id)
    if folder:
        if user.id == folder.user.id:
            return folder
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Folder not found")

@router.patch("/folder/{id}/", response_model=ResponseFolder)
async def update_folder(id: int, folder: PatchFolder, user: User = Depends(authorization)):
    db_folder = await Folder.objects.get_or_none(id=id)
    if db_folder:
        if user.id == db_folder.user.id:
            update_data = folder.dict(exclude_unset=True)
            return await db_folder.update(**update_data)
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Folder not found")

@router.post("/folder/{id}/add/{bookmark_id}", response_model=ResponseFolder)
async def add_to_folder(id: int, bookmark_id: int, user: User = Depends(authorization)):
    db_folder = await Folder.objects.get_or_none(id=id)
    if not db_folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    bookmark = await Bookmark.objects.get_or_none(id=bookmark_id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    if user.id != db_folder.user.id or user.id != bookmark.user.id:
        raise HTTPException(status_code=401, detail="Not authorized")

    await db_folder.bookmarks.add(bookmark)
    return db_folder

@router.post("/folder/{id}/remove/{bookmark_id}", response_model=ResponseFolder)
async def remove_from_folder(id: int, bookmark_id: int, user: User = Depends(authorization)):
    db_folder = await Folder.objects.get_or_none(id=id)
    if not db_folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    bookmark = await db_folder.bookmarks.get_or_none(id=bookmark_id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    if user.id != db_folder.user.id or user.id != bookmark.user.id:
        raise HTTPException(status_code=401, detail="Not authorized")

    await db_folder.bookmarks.remove(bookmark)
    return db_folder

@router.delete("/folder/{id}/", response_model=SuccessResponse)
async def delete_folder(id: int, user: User = Depends(authorization)):
    db_folder = await Folder.objects.get_or_none(id=id)
    if db_folder:
        if user.id == db_folder.user.id:
            # clear removes relationship from related bookmarks
            await db_folder.clear().delete()
            return SuccessResponse(detail="Folder successfully deleted")
        raise HTTPException(status_code=401, detail="Not authorized")
    raise HTTPException(status_code=404, detail="Folder not found")
