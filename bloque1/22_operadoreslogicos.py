# operadores logicos y multiples condiciones

"""

    and Y
    or o
    ! negacion 
    not no

"""

edad_minima = 18
edad_maxima = 65
"""edad_oficial = int(input("Cuantos años tienes? "))

if edad_oficial >= 18 and edad_oficial <= edad_maxima:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")"""


# otro ejemplo

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana") 


# otro ejemplo

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana") 


# otro ejemplo

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana") 