# a;adir valores a una lista mientras que la longitud sea menor a 120
# usar while y for

numero = 0
numeros = []

# while
print("---WHILE---")
while(numero <= 120):
    numeros.append(numero)
    numero += 1
print(numeros)

# for
numeros = []
for i in range(120 + 1):
    numeros.append(i)

print(numeros)

    