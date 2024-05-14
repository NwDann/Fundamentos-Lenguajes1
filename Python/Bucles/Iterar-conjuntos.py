# Iteraciones

animales = {'perro', 'gato', 'loro', 'oso'}

numeros = {75, 41, 25, 84}

for animal in animales:
    print(f"El animal es: {animal}")
    
for numero in numeros:
    print(numero * 10)
    
# Iteración de dos conjuntos al mismo tiempo, las conjuntos deben tener el mismo tamaño

#   variable 1 y 2        conjunto 1 y 2
for animal, numero in zip(animales, numeros):
    print(f"Recorriendo conjunto 1: {animal}")
    print(f"Recorriendo conjunto 2: {numero}")

# RANGE: Permite iterar en un for

for i in range(10, 15):
    print(i)

for i in range(5): # Itera de 0 a 5
    print(i)

# ENUMERATE: Forma correcta de recorrer una conjunto con su indice

for numero in enumerate(numeros):
    indice = numero[0]                         # numero ahora es una tupla (indice, valor)
    valor = numero[1]
    print(f"El indice es: {indice}, y el valor es: {valor}")
    
# Forma elegante de iterar una conjunto desempaquetando enumerate en el for
for indice, numero in enumerate(numeros):
    print(f"El indice es: {indice} y el valor es: {numero}")

# ELSE: Al final del for,y al ejecutar se muestra una sola vez al final del bucle, no importa que la conjunto a recorrer este vacia

for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual {numero}")
    
else:
    print("EL bucle ha terminado")
    
# TOdO LO ANTERIOR FUNCIONA DE IGUAL FORMA CON TUPLAS