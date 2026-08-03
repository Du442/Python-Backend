import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute(
    "INSERT INTO estudantes (nome, idade)\
    VALUES (?, ?)", ("João", 20)
)

conn.commit()

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

conn.close()