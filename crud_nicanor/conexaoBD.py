import mysql.connector
# Conexao com o Banco de Dados
conexao = mysql.connector.connect(
     host='localhost',
     user='root',
     password='123',
     database='colegio'
)
cursor = conexao.cursor()
print("Conectado! ")










