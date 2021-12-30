from fastapi import HTTPException, APIRouter, Request, Depends
from .models import User, UserWriteModel, UserReadModel, LoginSchema
from typing import List
from .helpers import is_authorized
from pydantic import BaseModel

router = APIRouter()

@router.post("/account/create/", response_model=UserReadModel)
async def create_user(user: UserWriteModel):
    user_dict = user.dict()
    email = user_dict.get("email")
    if not await User.objects.get_or_none(email=email):
        return await User(**user_dict).save()
    raise HTTPException(status_code=400, detail="Email already registered")

@router.get("/users", response_model=List[UserReadModel])
async def get_users():
    return await User.objects.all()

@router.get("/user/{id}", response_model=UserReadModel)
async def get_users(id: int, request: Request, user: dict = Depends(is_authorized)):
    if not await User.objects.get_or_none(id=id):
        raise HTTPException(status_code=404, detail="User not found")
    return await User.objects.get(id=id)

@router.post("/account/login/", response_model=LoginSchema)
async def create_user(user: UserWriteModel):
    user_dict = user.dict()
    email = user_dict.get("email")
    user = await User.objects.get_or_none(email=email)
    if user:
        token = await user.login(user_dict.get("password"))
        if token is not None:
            return LoginSchema(token=token)
    raise HTTPException(status_code=400, detail="Credentials provided are invalid")
