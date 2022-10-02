# parametros opcionales
# return


def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"

        cadena += "resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"

        cadena += "division: " + str(division)
        cadena += "\n"

    return cadena

print(calculadora(5,5, True))