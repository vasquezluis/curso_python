# manejo de errores y excepciones
# susceptible a fallos / errores

# se puede colocar dentro de un try except que es lo equivalente a try catch

from typing import final


try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)

except:
    print("Ha ocurrido un error, mete bien el nombre")

# se puede agregar un else en caso de no haber errores

else:
    print("Todo ha ido muy bien")

# se puede agregar finally, detecta cuando ya haya terminado TODO

finally:
    print("FIN DE LA ITERACION")