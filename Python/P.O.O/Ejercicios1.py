# Crear una clase estudiante con atributos: Nombre, Edad y Grado. Necesitamos de un método que imprima:
# "El alumno (nombre) esta estudiando", instanciar el objeto por medio de interaccion del usuario.
# Si el usuario escribe "estudiar", se ejecuta el metodo estudiar (no sensitive case)

class Estudiante:
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El/La alumno/a {self.nombre} esta estudiando")
    
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

estudiante1 = Estudiante(nombre, edad, grado)

op = input("El estudiante tiene que?: ")

if(op.lower() == "estudiar"):
    estudiante1.estudiar()
    
else:
    print("MAL")