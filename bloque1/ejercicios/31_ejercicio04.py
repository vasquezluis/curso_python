# ejercicio 4

"""

    Pedir dos numeros al usuarios y hacer todas las operaciones basicas de una calculadora
    Mostrarlo por pantalla

"""

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

def operaciones(x, y):
    
    suma = x + y
    resta = x - y
    multi = x * y
    division = x / y

    return (suma, resta, multi, division)


print("Operaciones basicas")

resultado = operaciones(numero1, numero2)

print(f"La suma es: {resultado[0]}")
print(f"La resta es: {resultado[1]}")
print(f"La multiplicacion es: {resultado[2]}")
print(f"La division es: {resultado[3]}")