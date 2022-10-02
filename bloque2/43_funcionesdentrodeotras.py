# funciones dentro de otras funciones

def getNombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + '\n' + getApellidos(apellidos)
    return texto

print(devuelveTodo("Luis", "Vasquez"))