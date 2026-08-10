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
    matriculations = relationship(
        "Matriculation", back_populates="student", cascade="all, delete-orphan"
    )
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship(
        "Teachers", back_populates="student"
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
    student = relationship(
        "Student",
        back_populates='teachers',
        cascade='all, delete-orphan'
    )

class Disciplines(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True, index=True)
    discipline = Column(String, nullable=False)
    description = Column(String, nullable=False)
    matriculations = relationship(
        "Matriculation",
        back_populates='disciplines',
        cascade='all, delete-orphan'
    )

class Matriculation(Base):
    __tablename__ = 'matriculations'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(
        "Student",
        back_populates='matriculations'
    )
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
    discipline = relationship(
        "Disciplines",
        back_populates='matriculations'
    )
