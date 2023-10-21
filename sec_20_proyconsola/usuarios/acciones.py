# importar modelo de usuario
import usuarios.usuario as modelo
# importar acciones de notas
import notas.acciones

# clase para las acciones, registro, login
class acciones:

    # metodos

    def registro(self):
        
        print("\nTe vamos a registrar")

        # datos de usuario
        nombre = input("Cual es tu nombre: ")
        apellidos = input("Cuales son tus apellidos: ")
        email = input("Cual es tu email: ")
        password = input("Cual es tu contrasenia: ")

        # modelo de usuario
        usuario = modelo.usuario(nombre, apellidos, email, password)

        # registrar al usuario
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):

        print("\nRegistro en el sistema")

        try: 

            # datos de login
            email = input("Cual es tu email: ")
            password = input("Cual es tu contrasenia: ")

            # objeto
            usuario = modelo.usuario('','', email, password)
            login = usuario.identificar()

            # comprobar si el email es el mismo que devuelve el modelo de indentificar
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema, el {login[5]}")
                self.proximasAcciones(login)
        
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Email o password incorrecto.")
    

    def proximasAcciones(self, usuario):
        
        print("""
        Acciones disponibles:

            - Crear nota (crear)
            - Mostrar notas (mostrar)
            - Eliminar notas (eliminar)
            - Salir (salir)
        """)

        hazEl = notas.acciones.acciones()
        accion = input("Que quieres hacer? ")

        if accion.lower() == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        if accion.lower() == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!!")
            exit()
