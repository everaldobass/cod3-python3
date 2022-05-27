import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='colegio'
)
cursor = conexao.cursor()
print("Conectado! ")

# CRUD
"""
sql = 'INSERT INTO estudantes(dni, sexo, nomes, apelidos) VALUES("12345678","M" ,"Edson", "Edson Jose")'
cursor.execute(sql)
conexao.commit()
"""

# SELECT
"""
sql = "SELECT * FROM estudantes"
cursor.execute(sql)
resultado = cursor.fetchall()
print(resultado)

"""
# UPDATE
"""
sql = f'UPDATE estudantes SET apelidos = "Edson José Nascimento" WHERE apelidos = "Edson Jose" '
cursor.execute(sql)
conexao.commit()
"""


# DELETE
"""
sql = f'DELETE FROM estudantes WHERE id = 2'
cursor.execute(sql)
conexao.commit()
"""


cursor.close()
conexao.close()