# Snakecase: todo_separado_por_guiones
# Camelcase: primeraLetraEnMinusLoDemasEnMayus
# Pascalcase: TodasLetrasEnMayuscula         <-     POR DEFECTO

class Celular(): # Los parentesis dan a entender que el constuctor se ejecuta automaticamente
    marca = "Samsung"
    modelo = "S23"
    camara = "48mpx"   # Propiedades o atributos estaticos
    
    
celular1 = Celular() # Metodo para crear o instanciar un objeto

# Acceso a sus atributos
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)

# Cambio de valor en un atributo para el objeto
celular1.camara = "24mpx"
print(celular1.camara)


class CelularMetodoConstructor:
    def __init__(self, marca, modelo, camara):   # Este es el metodo constructor, se ejecuta siempre primero
        self.marca = marca    # self hace referencia a si mismo, ademas, se crean las propiedades automaticamente
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):                    # Los metodos necesitan como parametro self
        print(f"Estas llamando desde un {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste la llamada desde un {self.modelo}")

celular2 = CelularMetodoConstructor("Samsung", "S23", "48mpx") # No hace falta pasar self
celular3 = CelularMetodoConstructor("Apple", "Iphone15Pro", "24mpx")

celular2.cortar()

celular3.llamar()