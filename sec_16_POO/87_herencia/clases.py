class persona:
    """
    nombre
    apellidos
    altura
    edad
    """

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"


# heredar de la clase padre
class informatico(persona):
    """
    lenguajes
    experiencia
    """
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(delf):
        return "He reparado tu PC"


# heredar de informatico
class tecnicoRedes(informatico):

    def __init__(self):
        # acceder al constructor del padre
        super().__init__()
        self.auditarRedes = "experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando"