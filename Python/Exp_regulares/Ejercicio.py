
import re

texto = "Hola señores, mi numero es +593 8121-3158, +593 8121-3158"

pattern = r"\+\d{3}\s\d{4}-\d{4}"

# SUB reemplaza la cadena en donde se encontro la coincidencia con una nueva
reemplazo = re.sub(pattern, "(Numero oculto)", texto)
print(reemplazo)