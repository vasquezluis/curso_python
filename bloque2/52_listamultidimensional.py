# listas muldimensional

print("\n ******************* LISTADO DE CONTACTOS ******************* ")
contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Salvador',
        'salvador@gmail.com'
    ]
]

print(contactos)
# email de luis
print(contactos[1][1])
print("\n")

# mostrar cada nombre e email
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Correo: {elemento}")
    print('\n')