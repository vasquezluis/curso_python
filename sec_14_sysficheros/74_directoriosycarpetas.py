# usar modulo os para directorios
import os, shutil

# crear carpeta
if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("Ya existe el directorio")


# copiar carpeta
# ruta_original = "./micarpeta"
# ruta_nueva = "./micarpeta_copiada"
# shutil.copytree(ruta_original, ruta_nueva)

# borrar carpeta
# os.rmdir("./micarpeta_copiada")

# listar archivos de una carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./micarpeta")
for fichero in contenido:
    print("Fichero: " + fichero)