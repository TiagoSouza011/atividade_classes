import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="r00t",
        database="atividade_classes"
    )
    return mydb
