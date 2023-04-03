from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import
from backend.db.db_config import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    course_id = Column(Integer)
    role_id = Column(Integer)
