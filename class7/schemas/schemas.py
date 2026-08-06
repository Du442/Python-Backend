from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Integer

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
