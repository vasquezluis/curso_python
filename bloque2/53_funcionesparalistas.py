# funciones y metodos para listas

cantantes = ["2pac", "Drake", "Ariana Grande", "Julio Iglesias"]
numeros = [1, 2, 3, 4, 8, 5]

# ordenar la lista
print(numeros)
numeros.sort()
print(numeros)

# a;adir elementos
cantantes.append("Chino y Nacho")
print(cantantes)
cantantes.insert(1, "David Bisbal")
print(cantantes)

# eliminar elementos de una lista
cantantes.pop(1)
print(cantantes)
cantantes.remove("Chino y Nacho")
print(cantantes)

# dar la vuelta a una lista
numeros.reverse()
print(numeros)

# buscar dentro de una lista
print('Drake' in cantantes)

# contar elementos
print(cantantes)
print(len(cantantes))

# cuantas veces aparece un elemento en la lista
numeros.append(8)
print(numeros.count(8))

# conseguir indice
print(cantantes.index('Drake'))

# unir dos listas
cantantes.extend(numeros)
print(cantantes)