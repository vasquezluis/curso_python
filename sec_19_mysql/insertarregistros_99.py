from sqlite3 import Cursor
from conexion_96 import *

cursor = database.cursor()

# insertar registros
# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

# insercion masiva
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citreon', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]

cursor.executemany("INSERT INTO vehiculos VALUES(NULL, %s, %s, %s)", coches)

# hacer commit para guardar cambios
database.commit()