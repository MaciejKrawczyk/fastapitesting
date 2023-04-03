from typing import List

from pydantic import BaseModel


class AccountModel(BaseModel):
    acc_id: int
    first_name: str
    last_name: str
    assigned_courses: List
