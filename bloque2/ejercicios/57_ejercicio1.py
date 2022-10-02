# ejercicio uno del bloque 2

# programa que tenga una lista de 8 numeros enteros
# 1 recorrerla y mostrarla
# 2 ordenarla y mostrarla
# 3 mostrar la longitud
# 4 buscar elemento en base a lo que pida el usuario

from operator import index
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
usuario_input = int(input("Coloque el numero a buscar en la lista: "))
if usuario_input in numeros:
    print(f"El numero {usuario_input} si existe en la lista. En el indice {numeros.index(usuario_input)}")
else:
    print(f"El numero {usuario_input} Ni existe en la lista.")
