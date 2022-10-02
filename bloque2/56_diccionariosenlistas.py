# diccionarios dentro de listas

contactos = [
    {
        'nombre': 'Luis',
        'apellidos': 'Vasquez',
        'email': 'luis.com'
    },
    {
        'nombre': 'Antonio',
        'apellidos': 'Tiu',
        'email': 'antonio.com'
    },
    {
        'nombre': 'Eunbi',
        'apellidos': 'Kwon',
        'email': 'kwon.com'
    }
]

print(contactos[0]['nombre'])
print("\n")

print("----- Lista de contactos -----")
for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}")
    print(f"Apelldio: {contacto['apellidos']}")
    print(f"Email: {contacto['email']}")
    print("-----------------------")
