# Criando o banco de Dados
import tkinter as tk
import sqlite3
import pandas as pd

# Conexão com o banco de dados
conexao = sqlite3.connect('clientes.db')
con = conexao.cursor()

# Criando a tabela no banco
con.execute(''' CREATE TABLE clientes(
   nome text,
   sobrenome text,
   email text,
   telefone text
)''')
# Confirmando
conexao.commit()
# Fechar o banco de dados
conexao.close()

