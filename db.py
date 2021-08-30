import sqlite3

#conexão db
conn = sqlite3.connect('contatos.db')

#definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE contatos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone INTEGER
)
""")

conn.close()