from fastapi import HTTPException, APIRouter
from .models import Users

router = APIRouter()

RequestUser = Users.get_pydantic(exclude={"id", "is_active", "is_admin", "joined_date"})
ResponseUser = Users.get_pydantic(exclude={"password"})

@router.post("/account/create/", response_model=ResponseUser)
async def create_user(user: RequestUser):
    user_dict = user.dict()
    email = user_dict.get("email")
    if not await Users.objects.get_or_none(email=email):
        return await Users(**user_dict).save()
    raise HTTPException(status_code=400, detail="Email already registered")