# funciones predefinidas

nombre = "Luis Vasquez"

# funcion imprimir
print(nombre)

#tipo de dato
print(type(nombre))

# detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es una string")
else:
    print("No es una cadena")

# limpiar espacios
frase = "   mi contenido    "
print(frase)
# llamando a la funcion strip para limpiar espacios
print(frase.strip())

# eliminar variables
year = 2022
print(year)
# del year
print(year)

# compribar variable vacia
texto = " ff  "
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

# encontrar caracteres
fras = "La vida es bella"
print(fras.find("vida"))

# reemplazar palabras en una string
# dos parametros, a reemplazar y reemplazante
nueva_fras = fras.replace("vida", "moto")
print(nueva_fras)

# mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())