# importar conexion
import usuarios.conexion as conexion
# importar modulo de fecha
import datetime
# importar modulo para cifrar contrase;as
import hashlib

# variable de conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# clase usuario
class usuario:

    # constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    # metodo de registro
    def registrar(self):

        # cifrar contrase;a
        cifrado = hashlib.sha256()
        # update recibe un byte, no un string
        cifrado.update(self.password.encode('utf8'))

        # consulta sql y tupla de valores de usuarios
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s);"
        # usar el valor hexadecimal del cifrado
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        # capturar error de duplicacion de usuario
        try:
            # ejecutar consulta
            cursor.execute(sql, usuario)
            # guardar cambios
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        # retornar los cambios y los valores
        return result

    # metodo de identificacion
    def identificar(self):
        
        # comprobar si un usuario ya existe en la bdd
        sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"

        # cifrar contrase;a
        cifrado = hashlib.sha256()
        # update recibe un byte, no un string
        cifrado.update(self.password.encode('utf8'))

        # datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        # consulta
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result