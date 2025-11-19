import mysql.connector
def conectar():
    return mysql.connector.connect(
        host= "192.168.2.40",
        user= "lucas",
        password= "lucas.1",
        database="treino_lucas",
        port= 3306
    )
