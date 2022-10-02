# manejar multiples excepciones

try:
    numero = int(input("Dime el numero, elevarlo al cuadrado: "))
    print(f'El cuadrado es: ' + str(numero*numero))
# escepcion cuando numero no es un int
except TypeError:
    print("Debes convertir tus cadenas a enteros")
# escepcion cuando numero es una cadena
# except ValueError:
    # print("Introduce un numero, no una cadena")
# ver el tipo de error ocurre
except Exception as e:
    print(type(e))
    print("El error es: " , type(e).__name__)