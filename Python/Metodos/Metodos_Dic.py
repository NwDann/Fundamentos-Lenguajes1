diccionario = {
    'nombre' : 'Danny',
    'apellido' : 'IiI',
    'anio' : 100
}

# KEYS: Devuelve llaves y sirve para iterar las claves

claves = diccionario.keys()

print(claves)

# GET: Devuelve el valor de la clave pasada, no lanza excepcion

claves = diccionario.get('nombre')

print(claves)

# ITEMS: Devuelve los elementos del diccionario iterables

dic_iterable = diccionario.items()

print(dic_iterable)

# POP: Elimina algun elemento pasandole la clave

diccionario.pop('nombre')

print(diccionario)

# CLEAR: Elimina todo lo del diccionario

diccionario.clear()

print(diccionario)

