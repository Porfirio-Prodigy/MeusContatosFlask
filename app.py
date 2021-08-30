from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='public')

#DATABASE SETTINGS
#conexão db
conn = sqlite3.connect('contatos.db', check_same_thread=False)
#definindo um cursor
cursor = conn.cursor()

#ROUTES
@app.route('/index')
@app.route('/')
def index():

    #---ID---
    # lendo os dados
    cursor.execute("""
        SELECT id FROM contatos;
    """)
    conn.commit()
    id = ()
    for linha in cursor.fetchall():
        id += linha
    
    #---TELEFONE---
    # lendo os dados
    cursor.execute("""
        SELECT nome FROM contatos;
    """)
    conn.commit()
    nome = ()
    for linha in cursor.fetchall():
        nome += linha
    
    #---TELEFONE---
    # lendo os dados
    cursor.execute("""
        SELECT telefone FROM contatos;
    """)
    telefone = ()
    conn.commit()
    for linha in cursor.fetchall():
        telefone += linha

    lista = zip(id,nome, telefone)
    
    

    return render_template('index.html', lista=lista)


@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    telefone = request.form['telefone']
    
    cursor.execute("""
    INSERT INTO contatos (nome, telefone)
    VALUES (?,?)
    """, (nome, telefone))
    conn.commit()

    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    id = request.form['id']

    # excluir registro único
    cursor.execute("""
    DELETE FROM contatos
    WHERE id = ?
    """, (id))
    conn.commit()

    return redirect(url_for('index'))
    

#INIT
if __name__ == '__main__':
    app.debug = True
    app.run()