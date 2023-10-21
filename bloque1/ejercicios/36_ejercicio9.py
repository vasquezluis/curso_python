# ejercicio 9

"""

    Pedir numeros y mostrarlos en pantalla hasta que se introduzca 111

"""

numero = 0

while numero != 111:
    numero = int(input("Introduce un numero: "))
    if numero == 111:
        print("Saliendo del programa")
        break
    else:
        print(f"El numero introducido es: {numero}")