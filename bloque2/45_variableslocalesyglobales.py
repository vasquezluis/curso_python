# variables globales  locales

# variables locales solo dentro de las funciones
# variables globales en todos lados

frase = "Hola que hace?"

print(frase)

def holaMundo():
    #frase = "Hola mundo!"
    print(frase)

    year = 2021
    print(year) 

    # hacer global una variable de funcion
    global website
    website = 'luisvasquezweb.com'

    return "Dato devuelto: " + str(year) 

holaMundo()
print("FUERA: ", website)