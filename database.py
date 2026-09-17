import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="sistema_visitas"
    )