# ejercicio 6

"""

    Mostrar todas las tablas de multiplicar del 1 al 10

"""

print(f" ------------- TABLAS DE MULTIPLICAR ------------- ")

for i in range(1, 10+1):
    print(f"TABLA DE MULTIPLICAR DE {i}")
    for j in range(1, 10+1):
        print(f"{i} x {j} = {i*j}")
    print("\n")
    
