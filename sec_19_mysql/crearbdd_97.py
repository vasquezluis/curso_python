from conexion_96 import *

# cursor | permite ejecutar las consultas
cursor = database.cursor()

# crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python;")

# ver bases de datos
cursor.execute("SHOW DATABASES;")
for bd in cursor:
    print(bd)
