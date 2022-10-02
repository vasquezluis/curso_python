# sqlite ya viene dentro de la instalacion de python

#importar modulo
from math import prod
import sqlite3

# conexion
conexion = sqlite3.connect('./insertselect.db')

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

# insertar dato
cursor.execute("INSERT INTO productos VALUES(null, 'Producto1', 'Descripcion del producto', 550)")
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)

for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

# primer registro de la tabla
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)

# cerrar la conexion
conexion.close()