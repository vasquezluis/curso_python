## Diccionarios

my_dic = dict()
my_other_dic = {}

print(type(my_dic))
print(type(my_other_dic))


# relacion clave valor (objeto en js)
my_other_dic = {
    "nombre": "Luis",
    "apellido": "Vasquez",
    "edad": 24,
    "lenguajes": {"python", "swift", "kotlin"},
}

print(my_other_dic)
print(my_other_dic["edad"])
my_other_dic["edad"] = 15
print(my_other_dic["edad"])


# remover un dato
del my_other_dic["edad"]
print(my_other_dic)

# comprobar existencia
print("luis" in my_other_dic)
print("nombre" in my_other_dic)


#
print(my_other_dic.items())
print(my_other_dic.keys())
print(my_other_dic.values())

# crear diccionario nuevo sin valores
my_other_dic = {
    "nombre": "Luis",
    "apellido": "Vasquez",
    "edad": 24,
    "lenguajes": {"python", "swift", "kotlin"},
}
my_new_dic = dict.fromkeys(my_other_dic)
print(my_new_dic)
