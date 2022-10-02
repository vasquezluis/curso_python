# if anidados

# compruebe la mayoria de edad de una persona

nombre = "Luis Vasquez"
ciudad = "Barcelona"
continente = "Oceania"
edad = 18
mayoria_edad = 18

if edad >= 18:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print(f"El usuario no es europeo")
    else:
        print(f"Es europeo y es de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad")