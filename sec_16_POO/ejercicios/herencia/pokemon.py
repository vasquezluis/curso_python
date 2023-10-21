class pokemon:

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEstadoCapturado(self, estado):
        self.estadoCapturado = estado
    
    def setAltura(self, altura):
        self.altura = altura

    def getNombre(self):
        return self.nombre
    
    def getEstadoCapturado(self):
        return self.estadoCapturado
    
    def getAltura(self):
        return self.altura

class hoenn(pokemon):

    def __init__(self):
        self.region = "Hoenn"

    def getRegion(self):
        return self.region

class electrico(hoenn):

    def __init__(self):
        super().__init__()
        self.tipo = "Electrico"
    
    def ataque1(self, ataque1):
        self.ataque1 = ataque1
        return "El atque 1 es " + self.ataque1