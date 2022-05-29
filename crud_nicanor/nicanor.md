# Nicanor
- https://www.youtube.com/watch?v=8JET7Ap0EGg
- install mysql-connector-python

class DataBase:
    def __int__(self):
     self.con=mysql.connector.connect(
        host='localhost:3306',
        database='colegio',
        user='root',
        password='123'
    )
     self.cursor = self.con.cursor()
