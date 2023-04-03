from typing import Any

from pydantic import BaseModel


class ServiceResponseModel(BaseModel):
    data: Any
    success: bool = True
    message: str = ''
