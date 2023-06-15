import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="tiago1234",
        database="database15"
    )
    return mydb
