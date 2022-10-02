# usar opern del paquete io
from io import open
# para la direccion absoluta
import pathlib

# ruta absoluta
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

# abrir archivo | segundo parametro son los permisos
archivo = open(ruta, "a+")

# escribir en archivo
archivo.write("************ SOY UN TEXTO METIDO DESDE PYTHON ************\n")

# cerrar archivo
archivo.close()