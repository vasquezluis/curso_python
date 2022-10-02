# importar modelo constructor coche
from coche import coche

carro = coche("Amarrilo", "Renault", "Clio", 150, 200, 4)
carro1 = coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getColor())
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# detectar tipado | compararlo con el nombre de la clase
if type(carro3) == coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")