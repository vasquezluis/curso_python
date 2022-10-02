"""
    4 variables - lista, string, entero y boolena
    imprimir que tipo de variable es cada una

"""


def traducir_tipo(tipo):
    resultado = None
    if tipo == list:
        resultado = "LISTA"
    elif tipo == str:
        resultado = "TEXTO"
    elif tipo == int:
        resultado = "ENTERO"
    elif resultado == bool:
        resultado = "BOOLEANO"
    else:
        resultado = "OTRO TIPO"
    
    return resultado


def tipoDato(variable):
    test = isinstance(variable, type(variable))
    resultado = ""

    if test:
        resultado = f"Esta variable es de tipo: {traducir_tipo(type(variable))}"
    else:
        resultado = None

    return resultado

lista = [1,2,3,4,5,6,7,8,9]
titulo = "Master en python"
numero = 100
verdadero = True

print(tipoDato(lista))
print(tipoDato(titulo))
print(tipoDato(numero))
print(tipoDato(verdadero))
