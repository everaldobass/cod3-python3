# ***********************************************************
# BY NAME:Everaldo Nascimento
# PROJECT:CRUD em Python com SQLite|Formulário Python Tkinter 
# v: 1.0.0
#
# Autor:Usando Python
# https://youtu.be/7N25wyyJ7pc
# https://doc.qt.io/qtforpython/licenses.html
# ***********************************************************

# Importando o Sqlite
import sqlite3 as lite
 
# Criando a conexao
conexao = lite.connect('dados.db')

# Criando a tabela
with conexao:
    con =  conexao.cursor()
    con.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, obs TEXT)")
                
               
                
               
                
                
            

