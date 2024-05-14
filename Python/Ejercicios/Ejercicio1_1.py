# Persona en promedio dice 2 palabras por segundo
# a) Pedir al usuario un texto con x palabras y calcular el tiempo a demorar
# b) Cuantas palabras se dijo
# Si se tardo mas de un minuto, pedir que pare de hablar
# Dalto habla un 30% mas rapido, cuanto tardaria en decirlo?

velocidad_hablar = 2 #palabras/segundo

respuesta_usuario = input("Pasame un texto con x palabras:\n")

respuesta_separada = respuesta_usuario.split(' ')

numero_palabras = len(respuesta_separada)

tiempo_usuario =  round(numero_palabras / 2, 2)

velocidad_dalto = round(velocidad_hablar * 1.3, 2)

tiempo_dalto = round(numero_palabras / velocidad_dalto, 2)

print('----------------USUARIO----------------')
if tiempo_usuario > 60:
    print('Demoraste mas de un minuto, calmate')

print(f'El tiempo a demorar del usuario promedio es de {tiempo_usuario} segundo/s')
print(f'El usuario uso {numero_palabras} palabras en su texto')

print('----------------DALTO----------------')
print(f'EL tiempo a demorar de Dalto promedio es de {tiempo_dalto} segundo/s')
