# Entran todos en desorden, asi que se pide la edad de todos
# El mayor es el profesor y el menor el asistente

def compañeros():
    numero = int(input('Ingrese el numero de personas: '))
    lista = []
    for i in range (1, numero + 1):
        nombre = input(f'Ingrese el nombre del {i} compañero: ')
        edad = int(input('Ingrese la edad: '))
        lista.append((nombre, edad))
    return lista


# INICIO
lista = compañeros()

lista.sort(key = lambda x : x[1])
nombre_p, edad_p = lista[-1]
nombre_a, edad_a = lista[0]
print(f'El profesor es {nombre_p} con la edad de {edad_p}')
print(f'El asistente es {nombre_a} con la edad de {edad_a}')