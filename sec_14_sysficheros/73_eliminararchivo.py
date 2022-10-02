# usar opern del paquete io
from genericpath import isfile
from io import open
# para la direccion absoluta
import pathlib
# para copiar archivo
import shutil
# para eliminar archivo
import os
# para saber si un archivo existe
import os.path

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_cambiado.txt"

# eliminar archivo
# os.remove(ruta_nueva)

# path con os
print(os.path.abspath("./"))

# comprobar si archivo existe
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")