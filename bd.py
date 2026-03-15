import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="erp_user",
        password="@Ljz128521",
        database="erp_universidade"
    )