'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
# Fórmula del IMC= peso / (altura x 2)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular():
    print("Para calcular su Índice de Masa Corporal (IMC)")    
    # Intenta solicitar peso y altura y convertirlo a float, si no se entran cifras mensaje de error
    try:
        peso_str = input("Ingrese su peso en kilogramos: ")
        peso_float = float(peso_str.replace(',', '.'))  # Reemplazar ',' por '.' para permitir coma decimal
    
        altura_str = input("Ingrese su altura en metros: ")
        altura_float = float(altura_str.replace(',', '.'))  # Reemplazar ',' por '.' para permitir coma decimal
    
    # Calcular el IMC y almacenar el resultado el la variable 'imc'
        imc = calcular_imc(peso_float, altura_float)
 
        print(f"Su IMC es de: {imc}, pero eso no significa nada, lo importante es sentirse en forma :)")

    except ValueError: print("El valor ingresado no es valido")

# Ejecutar el programa
calcular()
    
