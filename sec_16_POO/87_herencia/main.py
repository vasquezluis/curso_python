# la herencia es la posibilidad de compartir atributos y metodos entre clases
# que diferentes clases hereden de otras

import clases

persona = clases.persona()
persona.setNombre("Luis")
persona.setApellidos("Vasquez")
persona.setAltura(160)
persona.setEdad(23)

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")

print(persona.hablar())

print("----------------------------------")

# informatico
informatico = clases.informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")

print(informatico.getLenguajes())
print(informatico.caminar())

print("----------------------------------")

# tecnico redes
tecnico = clases.tecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())