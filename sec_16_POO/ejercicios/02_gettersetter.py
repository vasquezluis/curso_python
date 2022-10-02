# ejercicio de getter y setter

class persona():

    # atributos
    nombre = "Luis"
    apellido = "Vasquez"
    edad = 23
    sexo = "masculino"
    calificacion = 6
    dpi = False
    estadoCivil = False

    # metodos
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellido
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad
    
    def setDPI(self, estado):
        if estado >= 18:
            self.dpi = True
        else:
            self.dpi = False
    
    def getDpi(self):
        return self.dpi

    def setEstadoCivil(self, estado):
        self.estadoCivil = estado

    def getEstadoCivil(self):
        return self.estadoCivil

    def aumentaCalificacion(self):
        self.calificacion += 1

    def getCalificacion(self):
        return self.calificacion

luis = persona()
luis.setEdad(24)

# imprimir valores
print("Mi nombre es: ", luis.getNombreCompleto())
print("Mi edad es: ", luis.getEdad())
luis.setDPI(23)
print("Necesito DPI: ", luis.getDpi())
print("Mi calificacion antes de estudiar es: ", luis.getCalificacion())
luis.aumentaCalificacion()
print("Mi calificacion despues de estudiar es: ", luis.getCalificacion())
luis.setEstadoCivil(True)
print("Mi estado civil es: ", luis.getEstadoCivil())

