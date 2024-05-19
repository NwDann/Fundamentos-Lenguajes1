
# Forma no optima de sumar valores

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

resultado = suma_lista([5, 3, 5])
print(resultado)

# Forma optima utilizando args

def suma_total1(nombre, *numeros):     # el asterisco antes denumeros convierte todos los parametros a recibir en uno solo, DEBE ESTAR AL FINAL
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma_total1('Ojo', 4, 5, 6)
print(resultado)

# Lo mismo de arriba pero utilizando * (args) como argumento

def suma_total2(numeros):
    print(*numeros)
    return sum([*numeros])

resultado = suma_total2([5, 8, 7, 1])
print(resultado)