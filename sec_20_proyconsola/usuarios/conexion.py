# importar modulo para mysql
import pymysql
import sys

def conectar():
    # conexion a la base de datos | puede generar error por los parametros
    try:
        database = pymysql.connect(
            host="localhost",
            user="admin",
            passwd="30889567aS?",
            database="master_python",
            port=3306
        )
    except pymysql.Error as e:
        print("Error: {e}")
        sys.exit(1)
    
    # objeto para consultas
    cursor = database.cursor()

    # retornar para tener acceso a la bdd y al cursor
    return [database, cursor]