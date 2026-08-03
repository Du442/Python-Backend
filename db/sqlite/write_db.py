import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# cursor.execute(
#     '''
#         INSERT INTO estudantes (nome, idade) \
#         VALUES (?, ?)
#     ''',
#     ('João', 15)
# )

cursor.execute(
    '''
        INSERT INTO discliplinas2 (
            estudante_id, nome_disciplina
        ) VALUES (?,?)
    ''',
    (1, 'Matemática')
)

conn.commit()
conn.close()