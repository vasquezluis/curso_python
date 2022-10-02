class coche:

    # atributos | propiedades
    # caracteristicas del coche
    color = 'rojo'
    marca = 'Ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    # constructor
    # para dar caractersticas a la clase cuando es invocada
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getInfo(self):
        info = "--- Informacion del coche ---"
        info += "\n Color: " + self.getColor()
        info += "\n Modelo: " + self.getMarca()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info