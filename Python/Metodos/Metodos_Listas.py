
# LIST: Crea una lista, se puede usar para crear una lista sin elementos

lista = list(["Hola", 'Danny', 123])

print(lista)

# LEN: devuelve cantidad de elementos de la lista

resultado = len(lista)

print(resultado)

# APPEND: Agregar elementos a la lista

lista.append("Adios")

print(lista)

# INSERT: Agregar un elemento a la lista en una posicion especifica

lista.insert(2, 'ADSUDHS')

print(lista)

# EXTEND: Agregar varios elementos a la lista

lista.extend([True, 1.73])

print(lista)

#POP: Elimina un elemento de la lista por indice

lista.pop(0) # -1 se elimina el ultimo elemento, -2 el penultimo elemento, etc

print(lista)

# REMOVE: Remover un elemento por su valor buscandolo, si no lo encuentra lanza excepcion

lista.remove(123)

print(lista)

# SORT: Ordena la lista, solo si tiene numeros o booleanos

lista_numerica = list([24, 1,False , 8, 32, 4, True])

lista_numerica.sort() # Ordenado de forma ascendente

print(lista_numerica)

lista_numerica.sort(reverse = True) # Ordenado de forma descendente

print(lista_numerica)

# REVERSE: Invierte los elementos de una lista

lista.reverse()

print(lista)

# INDEX: Busca si existe un elemento en la lista, si no lo encuentra, lanza una excepcion

elemento_encontrado = lista_numerica.index(8)

print(elemento_encontrado)

# CLEAR: Elimina todos los elementos de la lista