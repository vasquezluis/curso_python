### sets ###

my_set = set()

my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # inicialmente es un diccionario

my_other_set = {"Luis", "Antonio", 23}
print(type(my_other_set))

print(len(my_other_set))

# trabajar con sets
my_other_set.add("luiissee")
print(my_other_set)  # un set no es una estructura ordenada
my_other_set.add("luiissee")  # un set no admite repetidos
print(my_other_set)


print("luiissee" in my_other_set)  # si un elemento existe en un set
print("luiisse" in my_other_set)

my_other_set.remove("luiissee")  # eliminar un dato de un set
print(my_other_set)


# clear elimina todo
my_other_set.clear()
print(my_other_set)

# del eliminar el set del programa
del my_other_set

my_set = {"Luis", "Moure", 24}
my_list = list(my_set)
print(my_list)


# unir dos sets
my_other_set = {"python", "javascript", "typescript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# diferencia entre sets
print(my_new_set.difference(my_set))
