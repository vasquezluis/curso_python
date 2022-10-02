# ejercicio de manejo de errores y captura de excepciones

# programa que tenga una lista de 8 numeros enteros
# 1 recorrerla y mostrarla
# 2 ordenarla y mostrarla
# 3 mostrar la longitud
# 4 buscar elemento en base a lo que pida el usuario

from operator import index
from unittest import expectedFailure
from numpy import sort


numeros = [5,8,6,3,7,9,4,2]

def recorrerLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += str(elemento) + ' '

    return resultado

# 1
print(recorrerLista(numeros))

# 2
ordenados = sort(numeros)
print(recorrerLista(ordenados))

# 3
longitud = len(numeros)
print(longitud)

# 4
# usuario_input = int(input("Coloque el numero a buscar en la lista: "))

# try:   
#     search = numeros.index(usuario_input)
#     print(f"El numero {usuario_input} si existe en la lista. En el indice {search}")
# except:
#     print(f"El numero {usuario_input} No existe en la lista.")

# manejar multiples excepciones

try:
    numero = int(input("Dime el numero, elevarlo al cuadrado: "))
    print(f'El cuadrado es: ' + str(numero*numero))
# escepcion cuando numero no es un int
except :
    print("Debes convertir tus cadenas a enteros")
