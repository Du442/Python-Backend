from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Integer

from class7.models.models import Teachers

class Profile(BaseModel):
    id: int
    age: int
    address: str

    class Config:
        from_attributes = True

class CreateProfile(BaseModel):
    age: int
    address: str
    
class Student(BaseModel):
    id: int
    name: str
    profile: Optional[Profile] = None

    class Config:
        from_attributes = True

class CreateStudent(BaseModel):
    name: str
    email: str
    profile: CreateProfile

class Discipline(BaseModel):
    id: int
    discipline: str
    description: str

class DisciplineCreate(BaseModel):
    discipline: str
    description: str

class Matriculation(BaseModel):
    student_id: int
    discipline_id: int

    class Config:
        from_attributes = True

class MatriculationCreate(BaseModel):
    student_id: int
    discipline_id: int

class Teacher(BaseModel):
    teacher: str

    class Config:
        from_attributes = True

class CreateTeacher(BaseModel):
    teacher: str