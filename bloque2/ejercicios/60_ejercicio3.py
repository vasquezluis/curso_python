# programa que compruebe si una una variable esta vacia
# llenarla si esta vacia con  minuscula
# mostrarla en mayuscula

frase = "Hola, esta es la frase de relleno"

frase_usuario = input("Escribe una frase: ")

if len(frase_usuario) == 0:
    frase_usuario = frase

print(frase_usuario)