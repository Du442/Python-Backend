import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    '''
        UPDATE estudantes SET nome = ? WHERE \
        id = ?
    ''',
    ('Leandro', 2)
)
conn.commit()
conn.close()