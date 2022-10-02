from django.shortcuts import render, redirect, HttpResponse
from .models import Article

# Create your views here.

# MVC = Modelo Vista Controlador -> Acciones (metodos) 
# MVT = Modelo Template Vista -> Acciones (metodos)

# pagina de inicio
def index(request):

    act_year = 2022
    years = range(act_year, 2051)

    nombre = 'Luis Vasquez'

    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'miapp/index.html', {
            'title': 'Inicio',
            'years': years,
            'nombre': nombre,
            'lenguajes': lenguajes
        })

# crear funciones para vista
def hola_mundo(request):

    countries = ['Canada', 'USA', 'Mexico', 'Guatemala']

    return render(request, 'miapp/hola_mundo.html', {
        'title': 'Hola Mundo',
        'countries': countries
        })

# pagina
def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', nombre='Luis', apellidos='Vasquez')

    return render(request, 'miapp/pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ["Elemento 1", "Elemento 2", "Elemento 3"]
    })

# contacto
def contacto(request, nombre='', apellidos=''):

    html = ''

    if nombre and apellidos:
        html += "<p> El nombre completo es: </p>"
        html += f"<h3> {nombre} {apellidos} </h3>"

    return HttpResponse(f"<h2> Contacto </h2>" + html)
    # return render(request, 'miapp/contacto.html')


def blog(request):

    return render(request, 'miapp/blog.html')

def crear_articulo(request):

    articulo = Article(
        title = 'Primer articulo',
        content = 'Contenido del articulo',
        public = True
    )

    articulo.save()

    return HttpResponse('articulo creado', )
