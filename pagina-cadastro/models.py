from sqlalchemy import \
    Column, Integer, String, ForeignKey, column
from db import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(
            Integer, 
            primary_key=True, 
            index=True,
            autoincrement=True
        )
    
    nome = Column(
        String(100),
        nullable=False
    )

    idade = Column(
        Integer(),
        nullable=False
    )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'),
    )

    nome_disciplina = Column(
        String(100),
        nullable=False
    )