# usar opern del paquete io
from io import open
# para la direccion absoluta
import pathlib
# para copiar archivo
import shutil

# copiar archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)