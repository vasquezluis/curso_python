from django.shortcuts import render, redirect, HttpResponse
from .models import Article
from django.db.models import Q

# Create your views here.

# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

# pagina de inicio
def index(request):

    act_year = 2022
    years = range(act_year, 2051)

    nombre = "Luis Vasquez"

    lenguajes = ["JavaScript", "Python", "PHP", "C"]

    return render(
        request,
        "miapp/index.html",
        {"title": "Inicio", "years": years, "nombre": nombre, "lenguajes": lenguajes},
    )


# crear funciones para vista
def hola_mundo(request):

    countries = ["Canada", "USA", "Mexico", "Guatemala"]

    return render(
        request,
        "miapp/hola_mundo.html",
        {"title": "Hola Mundo", "countries": countries},
    )


# pagina
def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect("contacto", nombre="Luis", apellidos="Vasquez")

    return render(
        request,
        "miapp/pagina.html",
        {
            "texto": "Este es mi texto",
            "lista": ["Elemento 1", "Elemento 2", "Elemento 3"],
        },
    )


# contacto
def contacto(request, nombre="", apellidos=""):

    html = ""

    if nombre and apellidos:
        html += "<p> El nombre completo es: </p>"
        html += f"<h3> {nombre} {apellidos} </h3>"

    return HttpResponse(f"<h2> Contacto </h2>" + html)
    # return render(request, 'miapp/contacto.html')


def blog(request):

    return render(request, "miapp/blog.html")


def crear_articulo(request, title, content, public):

    articulo = Article(title=title, content=content, public=public)

    articulo.save()

    return HttpResponse(f"articulo creado: {articulo.title} - {articulo.content}")


def articulo(request):

    # capturar el error cuando no exista articulo
    try:
        # dato de la base de datos
        articulo = Article.objects.get(title="Superman", public=True)
        response = f"Articulo: {articulo.id}. {articulo.title}"
    except:
        response = "<h2>Articulo no encontrado</h2>"

    return HttpResponse(response)


def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(
        f"articulo {articulo.id} editado: {articulo.title} - {articulo.content}"
    )


def articulos(request):

    # aplicar condicion y limite
    articulos = Article.objects.all().order_by('-id')

    """
    # utilizar lookup para filtros __
    articulos = Article.objects.filter(id__gte=4, title__contains="articulo")

    # exclude - excluir por filtro
    articulos = Article.objects.filter(title="Articulo").exclude(public=False)

    """
    # sql en django
    # articulos = Article.objects.raw(
    #     "SELECT * FROM miapp_article WHERE title='Articulo 2' AND public = 0"
    # )

    # OR en el ORM
    # articulos = Article.objects.filter(Q(title__contains="2") | Q(public=True))

    return render(request, "miapp/articulos.html", {"articulos": articulos})


def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect("articulos")


# formularios
def save_article(request):

    if request.method == "POST":

        title = request.POST["title"]
        content = request.POST["content"]
        public = request.POST["public"]

        articulo = Article(title=title, content=content, public=public)

        articulo.save()
        return HttpResponse(f"articulo creado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):

    return render(request, "miapp/create_article.html")
