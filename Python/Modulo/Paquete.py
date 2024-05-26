
import Paquetes.Saludar

# aparecera class 'list' si lo reconoce como un paquete y tiene el file __init__.py
print(type(Paquetes.__path__))

print(Paquetes.Saludar.saludar('Hola'))