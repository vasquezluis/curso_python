# clase perro

class perro():

    # atributos
    nombre = "Bobby"
    raza = "normal"
    altura = "1"
    edad = 1

    # metodos
    def comer():
        estado = "comiendo"
        return estado
    def dormir():
        estado = "durmiendo"
        return estado
    def ladrar():
        estado = "ladrando"
        return estado
    def edadAumenta(self):
        self.edad += 1

perro1 = perro()

# uso de la clase
print("El nombre del perro es: ", perro1.nombre)
print("La edad actual es: ", perro1.edad)
perro1.edadAumenta()
print("La edad actual del perro es: ", perro1.edad)