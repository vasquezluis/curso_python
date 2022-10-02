# ejercicio 5

"""

    Mostrar numeros entre dos numeros que el usuario decida

"""

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero2 > numero1:
    for i in range(numero1+1, numero2):
        print(f"El numero es: {i}")
else:
    print("El numero 1 tiene que ser menos al numero 2")