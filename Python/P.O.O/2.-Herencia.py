
class Persona:
    
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Como te va?, estoy hablando contigo")
        
class Empleado(Persona):
    #pass # Crear una clase o funcion que no haga nada
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self): # Sobreescritura del metodo hablar originario de la clase persona
        print(" Ya no quiero hablar")

class Estudiante(Persona):
    #pass # Crear una clase o funcion que no haga nada
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


Roberto = Empleado("Roberto", 24, "ecuatoriano", "Conductor", 1000)
print(Roberto.nombre)

Roberto.hablar()