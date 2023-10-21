# usar opern del paquete io
from io import open
# para la direccion absoluta
import pathlib
# para copiar archivo
import shutil

# mover archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_cambiado.txt"

shutil.move(ruta_original, ruta_nueva)