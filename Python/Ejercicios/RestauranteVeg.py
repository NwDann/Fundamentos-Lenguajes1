   
def menu_vegetariano()->float:
    print("                         MENU VEGETARIANO\n")
    print("1.- Hamburguesa de lentejas: Servida con pan integral, lechuga, tomate y salsa de yogur.")
    print("    8.50$")
    print("2.- Ensalada de Quinoa y Vegetales asados: Servida con aguacate, nueces y vinagreta balsámica.")
    print("    9.00$")
    print("3.- Wrap de Falafel: Servida con hummus, verduras frescas y salsa de tahini.")
    print("    7.75$")
    respuesta = int(input("Ingrese una opcion (1, 2 o 3): "))
    
    if respuesta == 1:
        total = 8.50
    elif respuesta == 2:
        total = 9
    elif respuesta == 3:
        total = 7.75
    
    print("                      INGREDIENTE ADICIONAL\n")
    print("1.- Aguacate: $1.00")
    print("2.- Queso Feta: $0.75")
    print("3.- Champiñones Salteados: $0.50")
    respuesta = int(input("Ingrese una opcion (1, 2 o 3): "))
    
    if respuesta == 1:
        total += 1
    elif respuesta == 2:
        total += 0.75
    elif respuesta == 3:
        total = 0.5
    
    print("                            BEBIDA\n")
    print("1.- Agua de Frutas Naturales: $2.00")
    print("2.- Té Helado: $1.50")
    respuesta = int(input("Ingrese una opcion (1 o 2): "))
    
    if respuesta == 1:
        total += 2
    elif respuesta == 2:
        total += 1.5
    
    return total
    
    
def menu_tradicional()->float:
    print("                         MENU TRADICIONAL\n")
    print("1.- Filete de Ternera a la Parrilla: Acompañado de puré de papas y vegetales al vapor.")
    print("    12.00$")
    print("2.- Pollo al Horno con Hierbas: Acompañada de arroz pilaf y espárragos.")
    print("    10.50$")
    print("3.- Lasaña de Carne: Servida con salsa de tomate, queso mozzarella y ricotta.")
    print("    11.25$")
    respuesta = int(input("Ingrese una opcion (1, 2 o 3): "))
    
    if respuesta == 1:
        total = 12
    elif respuesta == 2:
        total = 10.5
    elif respuesta == 3:
        total = 11.25
    
    print("                      INGREDIENTE ADICIONAL\n")
    print("1.- Tocino Ahumado: $1.25")
    print("2.- Queso Cheddar: $0.75")
    print("3.- Cebolla Caramelizada: $0.50")
    respuesta = int(input("Ingrese una opcion (1, 2 o 3): "))
    
    if respuesta == 1:
        total += 1.25
    elif respuesta == 2:
        total += 0.75
    elif respuesta == 3:
        total = 0.5
    
    print("                            BEBIDA\n")
    print("1.- Refresco de Cola: $1.75")
    print("2.- Limonada Fresca: $2.25")
    respuesta = int(input("Ingrese una opcion (1 o 2): "))
    
    if respuesta == 1:
        total += 1.75
    elif respuesta == 2:
        total += 2.25
    
    return total


print("              RESTAURANTE BINARIO")
print("Para mejorar su experiencia de usuario nos gustaria hacerte una pregunta.")

respuesta = int(input("¿Eres vegetariano? (Ingresa 1 o 2)\n1.- Si\n2.- No\n"))

if respuesta == 1:
    print("Esta bien, te presentaremos el menu vegetariano a continuacion:")
    total = menu_vegetariano()
    
elif respuesta == 2:
    print("Esta bien, te presentaremos el menu tradicional a continuacion:")
    total = menu_tradicional()

print("El total a pagar es: ", total)   