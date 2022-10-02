# ciclo for

"""

    for variable in elemento_iterable (lista, ranto, etc)
        BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado = 0

for contador in range(0,10):
    print(f"Voy por el " + str(contador))
    resultado += contador

print(f"El resultado es {resultado}")

# ejemplo - tabla de multiplicar

numero_usuario = int(input("De que numero quieres la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1
print(f"Tabla de multiplicar del numero {numero_usuario}")

for numero_tabla in range(0,10):

    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break
    print(f"{numero_usuario} x {numero_tabla + 1} = ", numero_usuario*(numero_tabla+1))
else:
    print("*****Tabla finalizada*****")

