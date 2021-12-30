from pydantic import BaseModel
from typing import Optional

class SuccessResponse(BaseModel):
    detail: Optional[str] = "Successfully performed operation"
