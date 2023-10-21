# importar modulo para mysql
import pymysql
import sys

# crear conexion
try:
    database = pymysql.connect(
        user="admin",
        passwd="30889567aS?",
        host="localhost",
        db="master_python"
        )
    
    print("Conexion establecida")
except pymysql.Error as e:
    print(f"Error en la conexion {e}")
    sys.exit(1)
