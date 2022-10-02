# ejercicio 8

"""

    Sacar el tanto porciento de otro numero que introduzca el usuario

"""

numero1 = int(input("Introduce el numero: "))
numero2 = int(input("Introduce el porcentaje: "))

porcentaje = numero2/100
total = numero1 * porcentaje

print(f"El porcentaje {numero2} de {numero1} es: {total}")