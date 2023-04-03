from fastapi import FastAPI

from models.ServiceResponse import ServiceResponseModel
from models.accounts.Student import StudentModel
from models.accounts.Teacher import TeacherModel
from backend.models.db.tables.Students import User
from sqlalchemy.orm import Session


app = FastAPI()


students = []
teachers = []


@app.get("/get-students", response_model=ServiceResponseModel)
async def get_students(db: Session):
    response = ServiceResponseModel()
    query = db.query(User).filter(User.role_id)
    response.data = query
    return response



@app.get("/get-teachers", response_model=ServiceResponseModel)
async def get_teachers():
    response = ServiceResponseModel()
    response.data = teachers
    return response


@app.post("/add-teacher", response_model=ServiceResponseModel)
async def say_hello(teacher: TeacherModel):
    response = ServiceResponseModel()
    teachers.append(teacher)
    response.data = teachers
    return response


@app.post("/add-student", response_model=ServiceResponseModel)
async def say_hello(student: StudentModel):
    response = ServiceResponseModel()
    students.append(student)
    response.data = students
    return response
