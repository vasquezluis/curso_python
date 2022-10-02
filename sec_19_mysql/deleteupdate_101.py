from conexion_96 import *

# cursor = database.cursor(buffered=True) #buffered para cuando se usa mucho el cursor()
cursor = database.cursor()

# borrar datos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes';")

database.commit()

# mostrar que ha borrado
print(cursor.rowcount, "borrados")

# actualizar datos
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat';")
database.commit()
print(cursor.rowcount, "actualizado")