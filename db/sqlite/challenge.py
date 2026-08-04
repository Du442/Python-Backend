import sqlite3

def conexao():
    conn = sqlite3.connect('loja.db')
    return conn

def create_table():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco FLOAT
        )    
    '''
    )
    conn.commit()
    conn.close()

def adicionar_produto(nome, preco):
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(
        '''
            INSERT INTO produtos (nome, preco)
            VALUES (?, ?)
        ''', (nome, preco))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM produtos
    ''')

    produtos = cursor.fetchall()
    for i in produtos:
        print(i)

    conn.commit()
    conn.close()
