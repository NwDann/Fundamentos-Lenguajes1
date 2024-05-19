
# DEF: Funcion simple

def saludar():
    print("Hola")

saludar()

# Funcion con parametros

def saludar_par(nombre : str):
    print(f'Hola {nombre}')
    
saludar_par('aquiz')

# Funcion que retorna valores, contrasenia

def contraseniar(numero):
    chars = 'sgdfgdf'
    numero_e = str(numero)
    num = int(numero_e[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contra = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contra, num  # Tupla
    
password, num = contraseniar(17)
print(f"Contraseña: {password}")
print(f'Numero utilizado: {num}')
