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
        "profile", back_populates="student", uselist=False, cascade="all, delete-orphan"
    )
    disciplines = relationship(
        "disciplines", back_populates="student", secondary='matriculations'
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
    teacher = Column(String, nullable=False)
    disciplines = relationship(
        "Disciplines", back_populates="Teachers"
    )

class Disciplines(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True, index=True)
    discipline = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

class Matriculation(Base):
    __tablename__ = 'matriculations'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
