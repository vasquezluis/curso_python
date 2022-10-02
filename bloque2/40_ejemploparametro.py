# mas ejemplos de funciones con parametros

# funcion que saque la tabla de multiplicar que se le pase por parametro


def tabla(numero):
    for i in range(1,10+1):
        print(f"{numero} x {i} = {numero*i}")

numero = int(input("Introduce un numero: "))

tabla(numero)