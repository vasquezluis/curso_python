# clase para una banda

from os import link


class banda():

    # atributos
    nombre = "Linkin Park"
    anio = 15
    cancion = "Guilty all the same"

    # metodo
    def getNombre(self):
        return self.nombre
    
    def getCancion(self):
        return self.cancion
    
    def setAnio(self):
        self.anio += 1
    
    def getAnio(self):
        return self.anio

linkin = banda()

print("La banda es: ", linkin.getNombre())
print("Una de las canciones es: ", linkin.getCancion())
print("Este a;o la banda tiene ", linkin.getAnio(), 'anios')
linkin.setAnio()
print("El siguiente a;o la banda tendra ", linkin.getAnio())