import Modulo.Funciones_ejemplo.Saludar as Saludar  # Modulo_saludar es un namespace
import Modulo.Funciones_ejemplo.Saludar as saludar #Renombrarlo como saludar

resultado = saludar.saludar('Perry')
print(resultado)
print(type(saludar))

from Modulo.Funciones_ejemplo.Saludar import saludar, saludar_raro as saludar_feo # Importamos SOLO una cosa (objeto, clase, propiedad, metodo) del modulo 
print(saludar('OJO'))
print(saludar_feo('No'))

# Acceso al nombre del modulo utilizado
print(__name__)