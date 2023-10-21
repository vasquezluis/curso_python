# multiples objetos

class coche:

    # atributos | propiedades
    # caracteristicas del coche
    color = 'rojo'
    marca = 'Ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

    def getColor(self):
        return self.color
    
    def getMarca(self):
        return self.marca
    
    # fin definicion de clase

# usar la clase | instanciar la clase
coche1 = coche()

print(coche1.getMarca(), coche1.getColor())
print("Velocidad actual: ", coche1.getVelocidad())
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()
print("velocidad nueva: ", coche1.getVelocidad())

print("COCHE 2")

# crear coche 2
coche2 = coche()
print(coche2.getColor())

