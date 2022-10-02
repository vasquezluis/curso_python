# getters y setters

class coche:

    # atributos | propiedades
    # caracteristicas del coche
    color = 'rojo'
    marca = 'Ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos, acciones que hace el objeto (funciones)
    # usar self para obtener los atributos de la clase
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    # fin definicion de clase

# usar la clase | instanciar la clase
coche = coche()

coche.setColor("negro")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
# usar getter para obtener una velocidad
print("Velocidad actual: ", coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("velocidad nueva: ", coche.getVelocidad())