"""
    Proyecto python y mysql

    - abrir asistente
    - login o registro
    - si elegimos registro, crear un usuario en la bdd
    - si elegimon login, identifica al usuario y nos preguntara
    - crear nota, mostrar notas, borrar notas

"""

from usuarios import acciones

# instanciar clase acciones
hazEl = acciones.acciones()

# Lo primero en imprimir
print("""
Acciones disponibles:

    - Registro
    - Login
""")

# variable para accion del usuarios
accion = input("Que quieres hacer? ")

if accion.lower() == "registro":

    # usar paquete usario
    hazEl.registro()

elif accion.lower() == "login":
    
    # usar paquete usuario
    hazEl.login()

