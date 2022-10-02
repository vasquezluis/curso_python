# sqlite ya viene dentro de la instalacion de python

#importar modulo
import sqlite3

# conexion
conexion = sqlite3.connect('conexion.db')

# crear cursor
cursor = conexion.cursor()

# crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"descripcion TEXT,"+
"precio INT(255)"+
")")

# guardar cambios
conexion.commit()

# cerrar la conexion
conexion.close()