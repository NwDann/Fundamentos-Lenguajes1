
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# LAMBDA: Las funciones lambda se pueden almacenar en variables

multiplicar_dos = lambda x : x * 2

print(multiplicar_dos(5))

# FILTER: Funcion comun, devuelve una lista de true o false recibiendo el nombre de la funcion y el parametro

def es_par(num):
    if (num % 2 == 0):
        return True
    
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# Numeros pares con Lambda

numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares))