cadena1 = "Hola soy Danny"
cadena2 = "Que tal"

# DIR: muestra los metodos propios del dato que se le da, lista de atributos validos

resultado = dir(cadena1) 

print(resultado)

#UPPER: Convierte el texto en mayusculas

resultado = cadena1.upper() 

print(resultado)

#LOWER: Convierte el texto en minusculas

resultado = cadena1.lower() 

print(resultado)

#CAPITALIZE: Convierte la primera letra en mayuscula

resultado = cadena1.capitalize() 

print(resultado)

#FIND: Buscar una cadena en otra cadena de texto y devuelve la posicion si la encuentra, si no -1

busqueda_find = cadena1.find('soy') 

print(busqueda_find)

#INDEX: Buscamos una cadena en otra cadena, si no lo encuentra, tira una excepcion

busqueda_index = cadena1.index('o') 

print(busqueda_index)

#ISNUMERIC: Si es numerico, devuelve True, aunque sea string

es_num = cadena1.isnumeric()

print(es_num)

#ISALFANUMERIC: Si es alfanumerico, devuelve True, aunque sea string. Solo son validos caracteres de A-z, no permitido espacios ni caracteres especiales

es_alfanum = cadena1.isalpha()

print(es_alfanum)

#COUNT: Devuelve el numero de coincidencias de la cadena buscada

contar_coincidencias = cadena1.count('a')

print(contar_coincidencias)

# LEN: Contamos cuantos caracteres contiene una cadena

contar_caracteres = len(cadena1)

print(contar_caracteres)

# STARTSWITH: verifica si una cadena empieza con otra dada

empieza_con = cadena1.startswith('Ho')

print(empieza_con)

# ENDSWITH: Verifica si una cadena termina con otra dada

termina_con = cadena1.endswith('nny')

print(termina_con)

# REPLACE: Reemplaza un pedazo de la cadena ada por otra si es que encuentra la coincidencia

cadena_nueva = cadena1.replace('la', 'lu')

print(cadena_nueva)

# SPLIT: Separar cadenas con la cadena pasada

cadena_separada = cadena1.split(' ')

print(cadena_separada)