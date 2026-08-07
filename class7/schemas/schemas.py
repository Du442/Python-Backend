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

class Teacher(BaseModel):
    id: int
    teacher: str

    class Config:
        from_attributes = True

class CreateTeacher(BaseModel):
    teacher: str
    disciplines: Optional[Teachers] = None