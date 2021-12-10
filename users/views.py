from fastapi import HTTPException
from .models import Users
from project.main import app


RequestUser = Users.get_pydantic(exclude={"id", "is_active"})
ResponseUser = Users.get_pydantic(exclude={"password": ...})

@app.post("/account/create/", response_model=ResponseUser)
async def create_user(user: RequestUser):
    user_dict = user.dict()
    email = user_dict.get("email")
    if not await Users.objects.get_or_none(email=email):
        return await Users(**user_dict).save()
    raise HTTPException(status_code=400, detail="Email already registered")