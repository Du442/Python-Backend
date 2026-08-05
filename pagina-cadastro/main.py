from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session, session
from typing import List
import models
import schemas
from db import SessionLocal, engine

# Cria as tabelas no Postgresql
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.post('/matriculas/', response_model=schemas.MatriculaResponse)
def create_registration(registration: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_registration = models.Matricula(**registration.model_dump())
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

@app.get('/matricula/', response_model=List[schemas.MatriculaResponse])
def get_registrations(db: Session = Depends(get_db)):
    registrations = db.query(models.Matricula).all()
    return registrations

@app.get('/estudantes/{estudante_id}', response_model=schemas.EstudanteOut)
def get_student(estudante_id: schemas.EstudanteOut, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id.first())

    if not estudante:
        raise HTTPException(status_code=404, detail='Estudante não encontrado')
    
    return estudante