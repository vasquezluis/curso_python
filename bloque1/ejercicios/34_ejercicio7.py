# ejercicio 7

"""

    Imprimir los numeros impares entre dos numeros 

"""

numero1 = int(input("Ingresa el numero 1: "))
numero2 = int(input("Ingresa el numero 2: "))

for i in range(numero1+1, numero2):
    if i % 2 != 0:
        print(f"Numero impar: {i}")