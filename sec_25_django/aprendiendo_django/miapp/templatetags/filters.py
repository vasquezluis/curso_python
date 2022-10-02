# filtros personalizados

from django import template

register = template.Library()

# decorador
@register.filter(name='saludo')

def saludo(value):

    largo = ''
    if len(value) >= 8:
        largo = '<p> Tu nombre es muy largo </p>'

    return f"<h2 style='background: green; color:white;'> Bienvenido: {value} </h2>" + largo