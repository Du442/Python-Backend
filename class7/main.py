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
    
    return students

