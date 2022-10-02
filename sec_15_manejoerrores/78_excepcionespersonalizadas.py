# excepciones personalizadas
try:

    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        # generar error
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido {nombre} al master en Python.")

except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)