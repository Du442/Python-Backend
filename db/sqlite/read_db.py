import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# cursor.execute(
#     '''
#         SELECT * FROM estudantes;
#     '''
# )

cursor.execute(
    '''
        SELECT * FROM discliplinas2;
    '''
)

conn.commit()

disciplinas = cursor.fetchall()
for i in disciplinas:
    print(i)

# estudantes = cursor.fetchall()

# for i in estudantes:
#     print(i)

conn.close()
