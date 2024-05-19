
# El orden de los parametros al llamar una funcion importa, pero se puede forzar con =

def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

# Utilizando keyword parameters

resultado = frase(adjetivo ='Dan', nombre ='I', apellido = 'piola')
print(resultado)

# Declarando variables de parametro en la propia funcion

def frase2(nombre, apellido, adjetivo = 'tonto'):
    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

resultado = frase2('Dan', 'I', 'inteligente')
print(resultado)