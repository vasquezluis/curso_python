class espec:

    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo
    
    __condiciones = "Malas"
    
    def getInfor(self):
        resultado = "---- INFORMACION ----"
        resultado += "\nMarca: " + self.marca
        resultado += "\nColor: " + self.color
        resultado += "\nTipo: " + self.tipo

        return resultado

    def getPrivado(self):
        return self.__condiciones
