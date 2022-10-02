from conexion_96 import *

cursor = database.cursor()

# select many
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat';")
result = cursor.fetchall()
for coche in result:
    print(coche[1], coche[3])


# select one
cursor.execute("SELECT * FROM vehiculos;")
coche = cursor.fetchone()
print(coche)