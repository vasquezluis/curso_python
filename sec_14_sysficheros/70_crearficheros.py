# usar opern del paquete io
from io import open
# para la direccion absoluta
import pathlib

# ruta absoluta
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# abrir archivo | segundo parametro son los permisos
archivo_lectura = open(ruta, "r")

# leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    if not elemento.isnumeric():
        print("- " + elemento.upper())

for frase in lista:
    frase_lista = frase.split()
    print(frase_lista)