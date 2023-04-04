from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db_config import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    course_id = Column(Integer)
    role_id = Column(Integer, ForeignKey("roles.id"))

    roles = relationship("Roles", back_populates="user")


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    user = relationship("Users", back_populates="roles")

