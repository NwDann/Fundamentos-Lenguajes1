
# DICT: Funcion para crear diccionarios

diccionario = dict(nombre = 'Danny', apellido = 'Iniaguazo')

# Las listas no pueden ser claves, las tuplas si, los conjuntos tambien si usamos frozenset

diccionario2 = {('hola', 'adios') : 'juasjuas'}

diccionario3 = {frozenset(['hola', 'adios']) : 'juasjuas'}

# FROMKEYS: Crear un diccionario

diccionario4 = dict.fromkeys('nombre', 'no se') # nombre es un iterable

diccionario5 = dict.fromkeys(['nombre', 'apellido']) # Lo crea en este caso con las 2 claves sin valor en su interior

print(diccionario)

print(diccionario2)

print(diccionario3)

print(diccionario4)

print(diccionario5)