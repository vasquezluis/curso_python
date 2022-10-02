# clases y objetos
# molde para crear mas objetos con caracteristicas parecidas

# definir una clase | molde
# (coche) con caracteristicas similares

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
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    # fin definicion de clase

# usar la clase | instanciar la clase
coche = coche()

print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("velocidad nueva: ", coche.velocidad)