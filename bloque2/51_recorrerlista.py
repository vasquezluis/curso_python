# recorrer listas

pelicula = "Batman"
peliculas = ["Batman", "Spiderman", "The ring"]
cantantes = list(("Tupac", "Drake", "Jennifer Lopez"))
years = list(range(2020, 2050))
variada = ["Luis", 5, 5.6, True, "Vasquez"]

# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)

# indices
print(peliculas[1])
print(peliculas[-2])

# sublistas
print(cantantes[1:3])
print(cantantes[:2])

# a;adir
cantantes.append("Kase O")
cantantes.append("Linkin Park")
print(cantantes)

# recorrer listas
nueva_pelicula = ''
while nueva_pelicula != 'parar':
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)

print(" \n *************** Listado de peliculas *************** ")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")



