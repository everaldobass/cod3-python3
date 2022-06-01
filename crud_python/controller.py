# ***********************************************************
# BY NAME:Everaldo Nascimento
# PROJECT:CRUD em Python com SQLite|Formulário Python Tkinter 
# v: 1.0.0
#
# Autor:Usando Python
# https://youtu.be/7N25wyyJ7pc
# https://doc.qt.io/qtforpython/licenses.html
# ***********************************************************

# CRUD

# INSERIR

# Importando o Sqlite
import sqlite3 as lite
 
# Criando a conexao
conexao = lite.connect('dados.db')


# Criando a lista
# lista = ['Edson', 'edson@gmail.com', '123456789', "31/06/2022", 'Normal', 'Consulta online']
# Inserir
def inserir_info(i):
    with conexao:
         cur = conexao.cursor()
         query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, obs) VALUES (?, ?, ?, ?, ?, ?)"
         cur.execute(query,i)
# SELECT

def mostrar_info():
    lista = []
    with conexao:
         cur = conexao.cursor()
         query = "SELECT * FROM formulario"
         cur.execute(query)

         dados = cur.fetchall()

         for i in dados:
             lista.append(i)
    return lista
  
# Atualizar Formulario
def atualizar_info(i):
    with conexao:
         cur = conexao.cursor()
         query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, obs=? WHERE id=?"
         cur.execute(query,i)


# DELETE
def deletar_info(i):
    with conexao:
         cur = conexao.cursor()
         query = "DELETE FROM formulario WHERE id=?"
         cur.execute(query,i)


  
