'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.'''
def calcular_precio_final(precio_inicial):
    descuento = 0.2
    precio_final = precio_inicial * (1 - descuento)
    return precio_final

try:
    precio_inicial = float(input("Ingrese el precio al cual se aplicará un descuento del 20%: "))
    if precio_inicial <= 0:
        print("El precio debe ser mayor que cero")
    else:
        precio_final = calcular_precio_final(precio_inicial)
        print(f"El precio con 20% de descuento es: {precio_final:.2f}")# se imprime el precio final con 2 decimales
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

