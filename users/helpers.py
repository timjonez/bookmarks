from fastapi import HTTPException, Request
from bookmarker.settings import settings
import jwt

def is_authorized(request: Request):
    msg = "Not authorized"
    auth_token = request.headers.get("authorization")
    if auth_token is not None:
        try:
            data = jwt.decode(auth_token, settings.secret_key, algorithms="HS256")
            return data.get("email")
        except Exception as exc:
            if type(exc) == jwt.ExpiredSignatureError:
                msg = "Not authorized - token is expired"
    raise HTTPException(status_code=401, detail=msg)
