"""

    Crear una lista con el contenido de esta tabla

    ACCION  AVENTURA    DEPORTES
    GTA     ASSASSINS    FIFA 21    
    COD     CRASH       PRO 21
    PUBG    PRINCE      MOTO GP

    Mostrar informacion ordenada

"""

tabla = [
    {
        "Categoria": "ACCION",
        "Juegos": ["GTA", "COD", "PUBG"]
    },
    {
        "Categoria": "AVENTURA",
        "Juegos": ["Assasins", "Crash", "Price of Percia"]
    },
    {
        "Categoria": "DEPORTES",
        "Juegos": ["FIFA 21", "PRO 21", "MOTO GP"]
    }
]

for categoria in tabla:
    print(f"---------{categoria['Categoria']}---------")
    for juego in categoria['Juegos']:
        print(juego)

