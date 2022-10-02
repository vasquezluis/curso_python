class banda:

    def __init__(self, nombre, anio, album):
        self.nombre = nombre
        self.anio = anio
        self.album = album

    # atributo privado
    __debut = 1950
    
    def getInfo(self):
        result = "-- Banda --"
        result += "\nNombre: " + self.nombre
        result += "\nAnio: " + str(self.anio)
        result += "\nAlbum: " + self.album

        return result
    
    def getDebut(self):
        debut = "Debut: " + str(self.__debut)
        return debut
    