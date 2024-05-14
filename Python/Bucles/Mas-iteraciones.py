
frutas = ['manzana', 'granada', 'banana', 'uva', 'ciruela']
cadena = 'como te va'
numeros = [2, 5, 4, 1]

for fruta in frutas:
    if fruta == 'granada':    #CONTINUE: Hace que el bucle pase a la siguiente iteracion sin ejecutar lo demas
        continue              # Evita que se coma una granada
    print(f'Tengo ganas de una: {fruta}')

# BREAK: Termina todo el bucle

for fruta in frutas:
    if fruta == 'banana':   
        break                  
    print(f'Tengo ganas de una: {fruta}')

print('bucle terminado')

# El break hace que el else no se ejecute

for fruta in frutas:
    if fruta == 'banana':   
        break                  
    print(f'Tengo ganas de una: {fruta}')
else:
    print('bucle terminado')

# Recorrer una cadena de texto

for letra in cadena:
    print(letra)
    
# For en una sola linea de codigo

    # metodo tradicional
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)

    #lo mismo en una sola linea
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)