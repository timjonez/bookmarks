from fastapi import HTTPException, Request
from bookmarker.settings import settings
from .models import User
import jwt

def is_authorized(request: Request):
    msg = "Not authorized"
    auth_token = request.headers.get("authorization")
    if auth_token is not None:
        try:
            data = jwt.decode(auth_token, settings.secret_key, algorithms="HS256")
            return True
        except Exception as exc:
            if type(exc) == jwt.ExpiredSignatureError:
                msg = "Not authorized - token is expired"
    raise HTTPException(status_code=401, detail=msg)


async def authorization(request: Request) -> User:
    if is_authorized(request):
        auth_token = request.headers.get("authorization")
        data = jwt.decode(auth_token, settings.secret_key, algorithms="HS256")
        return await User.objects.get(email=data.get("email"))
    raise HTTPException(status_code=401, detail="Not authorized")
