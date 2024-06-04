
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")
        


try:
    raise MiExcepcion ("Se te fue de las manos") # Raise lanza una excepción e imprime el texto dentro del parentesis como causa

except:
    print("Como vas a cometer ese error")