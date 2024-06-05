class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Como te va?, estoy hablando contigo")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"mi habilidad es: {self.habilidad}"
    
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f"Hola, mi nombre es: {self.nombre}, {super().mostrar_habilidad()}, y trabajo en: {self.empresa}" 
    # Puedo poner self o super(), pero super hace referencia a metodos heredados, self a metodos propios de la clase
        
Roberto = EmpleadoArtista("Roberto", 24, "ecuatoriano", "Bailar", 1000, "Ecomoda")
print(Roberto.presentarse())

herencia = issubclass(EmpleadoArtista, Artista) # EmpleadoArtista es subclase de Artista?
print(herencia)

herencia = issubclass(Artista, Persona) # Artista es subclase de Persona? (hereda de)
print(herencia)

instancia = isinstance(Roberto, EmpleadoArtista) # Roberto es una instancia/objeto de EmpleadoArtista?
print(instancia)

instancia = isinstance(Roberto, Artista) # Roberto es una instancia/objeto de Artista? Si, porque hereda de este
instancia = isinstance(Roberto, Persona) # Roberto es una instancia/objeto de Persona? Si, porque hereda de este
print(instancia)