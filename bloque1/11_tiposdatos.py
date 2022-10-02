# tipos de datos


nada = None

#mostrar tipo de dato

print(type(nada))

# cadena
cadena = "Hola, esta es una cadena"
print(type(cadena))

# entero
entero = 94
print(type(entero))

# flotante
flotante = 4.2
print(type(flotante))

# booleano
booleano = True
print(type(booleano))

# lista
lista = [10, 20, 30, 100, 200]
print(type(lista))

# tupla, no cambian los datos
tupla = ('Master', 'en', 'python')
print(type(tupla))

# diccionario, clave y valor
diccionario = {
    "nombre": "luis",
    "apellido": "vasquez",
    "curso": "master en python"
}
print(type(diccionario))

# rango
rango = range(9)
print(rango)
print(type(range))

# byte
dato_byte = b"probando"
print(dato_byte)
print(type(dato_byte))