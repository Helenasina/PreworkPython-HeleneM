'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''
def calcular_area(longitud, ancho):
    return longitud * ancho

try:
    longitud = float(input("Ingresar longitud del rectángulo en cm: "))
    ancho = float(input("Ingresar ancho del rectángulo en cm: "))

    # Calcular el área del rectángulo y almacenarlo en la variable 'area'
    area = calcular_area(longitud, ancho)

    print(f"El área del rectángulo es: {area} cm2")

except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

