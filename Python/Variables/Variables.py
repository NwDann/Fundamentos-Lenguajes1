a = 5
b = 17
c = a + b
print(c)

# USOS SIMBOLO DE IGUALDAD

num = 10
num += 5
num -= 2
num /= 2
num *= 2
num **= 2
print(num)

#CONCATENACION

nombre = 'Papo'
print(nombre)
bienvenida = "Hola " + nombre + ", como estas?"  #No podemos concatenar un entero
print(bienvenida)

    #solucion
nombre = 5
bienvenida = f"Hola {nombre}, como estas?" #f strings: toma un dato, sea cuaqluiera, lo convierte a texto
print(bienvenida)
del nombre  #del: Borra datos alojados en memoria

# OPERADORES DE PERTENENCIA "IN" Y "NOT IN"

print("ola" in bienvenida) #Se utiliza parea buscar un pedazo de string en la variable, devuelve True o False
print("pedro" not in bienvenida)

# DECLARACION DE VARIABLES

    # Con camelCase
nombreDeMiAbuela = "Maria Hol"

    # Con snakeCase
nombre_de_mi_abuela = "Maria Hol"