
import re

texto = '''Joder buenos dias, este dia esta bastante soleado. Asi que deberias cuidarte
Bueno, esta es la segunda linea para recordarte abbbque compres 114 mandarinasabbbb. redes
Y aca anotare que el dia lunes (02. ) tengo algo relacionado con redes'''

# SEARCH: encuentra una coincidencia y la devuelve
resultado = re.search("dias", texto)

# FINDALL: encuentra coincidencias y las devuelve
resultado = re.findall("dia", texto, flags = re.IGNORECASE) # IGNORECASE ignora las mayusculas y minusculas en el texto

#\d -> Busca digitos numericos del 0 al 9, solo un numero (27 -> 2 y 7)
#resultado = re.findall(r"\d", texto)

#\D -> Busca TODO menos digitos numericos del 0 al 9 
#resultado = re.findall(r"\D", texto)

#\w -> Busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w", texto)

#\W -> Busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W", texto)

#\s -> Busca espacios en blanco, tabs o newlines (\n)
#resultado = re.findall(r"\s", texto)

#\S -> Busca TODO menos espacios en blanco, tabs o newlines (\n)
#resultado = re.findall(r"\S", texto)

#. -> Busca TODO menos saltos en linea
#resultado = re.findall(r".", texto)

#\n -> Busca saltos en linea
#resultado = re.findall(r"\n", texto)

#\ -> Cancelar caracteres especiales (no alfanumericos =, ?)
#resultado = re.findall(r"\.", texto) # Cancela la funcion de buscar todo menos \n y busca puntos

# Exp regular que encuentra el patron dado (1. )
#resultado = re.findall(r"\d\.\s", texto)

#^ -> Busca el comienzo de una linea
#resultado = re.findall(r"^Joder", texto)
#resultado = re.findall(r"^Bueno", texto, flags = re.M) # M significa multilinea

#$ -> Busca el final de una linea
#resultado = re.findall(r"redes$", texto)
#resultado = re.findall(r"redes$", texto, flags = re.M) 

#{n} -> Busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r"\d{3}", texto)

#{n, m} -> Busca al menos n y como maximo m cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{1,4}", texto)
resultado = re.findall(r"(ab){1,4}", texto) # Los parentesis representan grupos

#| -> Busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|dia", texto)

print(resultado)