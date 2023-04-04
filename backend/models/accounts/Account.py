from typing import List

from pydantic import BaseModel


class AccountModel(BaseModel):
    acc_id: int
    first_name: str
    last_name: str
    course_id: int
    role_id: int

    class Config:
        orm_mode = True


class AccountModelAdd(BaseModel):
    first_name: str
    last_name: str
    course_id: int
    role_id: int

    class Config:
        orm_mode = True