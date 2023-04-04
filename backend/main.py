from enum import Enum

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from db.db_config import get_db, engine, Base
from db.tables.Users import Users, Roles
from models.ServiceResponse import ServiceResponseModel
from models.accounts.Student import StudentModel, StudentModelAdd
from models.accounts.Teacher import TeacherModel, TeacherModelAdd
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["http://127.0.0.1:5173"]
# origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []
teachers = []


@app.get("/get-students", response_model=ServiceResponseModel)
async def get_students(db: Session = Depends(get_db)):
    response = ServiceResponseModel()
    query = db.query(Users).filter(Users.role_id == 2).all()
    response.data = query
    return response


@app.get("/get-teachers", response_model=ServiceResponseModel)
async def get_teachers(db: Session = Depends(get_db)):
    response = ServiceResponseModel()
    query = db.query(Users).filter(Users.role_id == 1).all()
    response.data = query
    return response


@app.post("/add-teacher", response_model=ServiceResponseModel)
async def say_hello(teacher: TeacherModelAdd, db: Session = Depends(get_db)):
    response = ServiceResponseModel()
    teacher_to_add = Users(first_name=teacher.first_name,
                           last_name=teacher.last_name,
                           course_id=teacher.course_id,
                           role_id=teacher.role_id)
    db.add(teacher_to_add)
    db.commit()
    response.data = db.query(Users).filter(Users.role_id == teacher.role_id).all()
    return response


@app.post("/add-student", response_model=ServiceResponseModel)
async def say_hello(student: StudentModelAdd, db: Session = Depends(get_db)):
    response = ServiceResponseModel()
    teacher_to_add = Users(first_name=student.first_name,
                           last_name=student.last_name,
                           course_id=student.course_id,
                           role_id=student.role_id)
    db.add(teacher_to_add)
    db.commit()
    response.data = db.query(Users).filter(Users.role_id == student.role_id).all()
    return response
