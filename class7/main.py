from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from connection.database import engine, SessionLocal
from typing import List
from sqlalchemy import joinedload
import schemas.schemas
import models.models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/register/', response_model=schemas.schemas.Student)
def create_student(
        student: schemas.schemas.CreateStudent, 
        db: Session = Depends(get_db)
    ):
    db_student = models.models.Student(
        name = student.name,
        profile = models.models.Profile(**student.profile.dict())
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/students/', response_model=List[schemas.schemas.Student])
def list_students(db: Session = Depends(get_db)):
    students = db.query(models.models.Student).options(
        joinedload(models.models.Student.profile)
    ).all()

    if not students:
        raise HTTPException(status_code=404, detail='Student not found')
    
    return students

# disciplines

@app.post('/disciplines/', response_model=schemas.schemas.Discipline)
def create_discipline(
        discipline: schemas.schemas.DisciplineCreate,
        db: Session = Depends(get_db)
    ):
    db_discipline = models.models.Disciplines(**discipline.dict())
    db.add(db_discipline)
    db.commit()
    db.refresh(db_discipline)
    return db_discipline

@app.get('/disciplines/', response_model=schemas.schemas.Discipline)
def list_disciplines(db: Session = Depends(get_db)):
    disciplines = db.query(models.models.Disciplines).all()
    
    if not disciplines:
        raise HTTPException(status_code=404, detail='Discipline not found')

    return disciplines

# teachers

@app.post('/teachers/', response_model=schemas.schemas.CreateTeacher)
def create_teacher(teacher: schemas.schemas.CreateTeacher, db: Session = Depends(get_db)):
    db_teacher = models.models.Teachers(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.get('/teachers/', response_model=schemas.schemas.Teacher)
def list_teachers(db: Session = Depends(get_db)):
    teachers = db.query(models.models.Teachers).all()

    if not teachers:
        raise HTTPException(status_code=404, detail='Teacher not found')

    return teachers

# matriculations


@app.post('/matriculations/', response_model=schemas.schemas.MatriculationCreate)
def create_teacher(matriculation: schemas.schemas.MatriculationCreate, db: Session = Depends(get_db)):
    db_matriculation = models.models.Matriculation(**matriculation.dict())
    db.add(db_matriculation)
    db.commit()
    db.refresh(db_matriculation)
    return db_matriculation

@app.get('/matriculations/', response_model=schemas.schemas.Matriculation)
def list_matriculations(db: Session = Depends(get_db)):
    matriculations = db.query(models.models.Matriculation).all()
    
    if not matriculations:
        raise HTTPException(status_code=404, detail='Matriculation not found')

    return matriculations