import sqlite3

conexion = sqlite3.connect('practica01.db')

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"nombre VARCHAR(50),"+
"apellidos TEXT,"+
"edad INT(3)"+
")")

conexion.commit()

cursor.execute("INSERT INTO usuarios VALUES(null, 'Luis Antonio', 'Vasquez Tiu', 23)")
conexion.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print("ID: ", usuario[0])
    print("Nombres: ", usuario[1])
    print("Apellidos: ", usuario[2])
    print("Edad: ", usuario[3])
    print("\n")


conexion.close()