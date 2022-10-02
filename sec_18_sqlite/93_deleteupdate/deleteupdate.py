# sqlite ya viene dentro de la instalacion de python

#importar modulo
import sqlite3

# conexion
conexion = sqlite3.connect('deleteupdate.db')

# crear cursor
cursor = conexion.cursor()

# crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255))
""")

# guardar cambios
conexion.commit()

# insertar dato
cursor.execute("INSERT INTO productos VALUES(null, 'Producto1', 'Descripcion del producto', 550)")
conexion.commit()

# borrar registros
cursor.execute("DELETE FROM productos;")
conexion.commit()

# insertar muchos registro a la vez
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES(null, ?, ?, ?)", productos)
conexion.commit()

# actualizar datos
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80;")


# listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
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