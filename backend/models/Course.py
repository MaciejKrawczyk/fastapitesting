from typing import List

from .models.accounts.Teacher import TeacherModel


class CourseModel:
    name: str
    admin: TeacherModel
    members: List
