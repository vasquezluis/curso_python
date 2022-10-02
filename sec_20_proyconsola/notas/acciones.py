# clase para las acciones de las notas

import  notas.nota as modelo


class acciones:

    def crear(self, usuario):

        print(f"\nOk {usuario[1]}, vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nHas guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota.")
    
    def mostrar(self, usuario):

        print(f"{usuario[1]}, aqui tienes tus notas")

        nota = modelo.nota(usuario[0])

        notas = nota.listar()

        for nota in notas:
            print("\n*****************")
            print(nota[2])
            print(nota[3])
            print("*****************")
    
    def borrar(self, usuario):

        print(f"\n{usuario[1]}, vamos a borrar una nota")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.nota(usuario[0], titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos eliminado la nota {nota.titulo}")
        else:
            print("No se ha eliminado la nota, prueba de nuevo")

        
