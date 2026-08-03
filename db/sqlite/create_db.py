import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    '''
)

cursor.execute(
    '''
        CREATE TABLE discliplinas2 (
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) \
                REFERENCES estudante(id)
        )
    '''
)

conn.commit()
conn.close()
