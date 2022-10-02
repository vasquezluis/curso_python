# getter y setter

class gato:

    # atributos
    nombre = "Mish"
    altura = 0.3
    genero = 'maculino'

    # metodos

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
    

michi1 = gato()

print(f"El nombre del gato es {michi1.getNombre()}")
michi1.setNombre("Lucas")
print(f"El nombre del gato es {michi1.getNombre()}")
