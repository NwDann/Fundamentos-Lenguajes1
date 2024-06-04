
def suma():
    while True:
        a = input("Dame un numero: ")
        b = input("Dame otro numero: ")
        try:
            resultado = int(a) + int(b)
            
        except Exception as e:
            print("NO INGRESES LETRAS")
            print(f"Error: {e}") # Cual fue el error
            print(f"Error: {type(e).__name__}") # Cual es el nombre del error
            
        else: # Else solo se ejecutara cuando try no nos lance una excepcion
            break
        
        finally: # Se ejecuta sin importar cual fue el resultado de los demas
            print("Esto se ejecuta siempre")
            
    return resultado

print(suma())