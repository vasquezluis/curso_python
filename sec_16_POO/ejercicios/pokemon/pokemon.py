# clase para pokemones

class pokemon:

    def __init__(self, nombre, altura, tipo):
        self.nombre = nombre
        self.altura = altura
        self.tipo = tipo

    
    def getInfo(self):
        resultado = "-- Datos del Pokemon --"
        resultado += "\nNombre: " + self.nombre
        resultado += "\nAltura: " + str(self.altura)
        resultado += "\nTipo: " + self.tipo

        return resultado
