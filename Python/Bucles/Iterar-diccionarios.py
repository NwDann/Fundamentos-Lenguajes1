
# Iteraciones

diccionario = {
    'nombre' : 'Danny',
    'apellido' : 'I'
}

print(diccionario)

# Iterar claves

for key in diccionario:
    print(key)

# ITEMS: Permite iterar el diccionario, tanto sus claves como valores

for key in diccionario.items():    # key es una tupla
    print(key)

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el dato es: {value}")