from re import T
from sqlalchemy import \
    Column, String, Integer, ForeignKey
from sqlalchemy import relationship
from connection.database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    profile = relationship(
        "Profile", back_populates="Student", uselist=False, cascade="all, delete-orphan"
    )

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    address = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    student = relationship(
        "Student", back_populates="Profile"
    )

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False)
    

class Disciplines(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True, index=True)
    discipline_name = Column(String, nullable=False)