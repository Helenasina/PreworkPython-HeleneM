'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''
def convertir_EUR_USD(cantidad_dolares):
    cantidad_euros = cantidad_dolares * 0.85
    return cantidad_euros
try:
    cantidad_dolares = float(input("Ingrese una cantidad a convertir de dólares a euros: "))
    cantidad_euros = convertir_EUR_USD(cantidad_dolares)

    print(f"{cantidad_dolares} dólares son {cantidad_euros} euros.")

except ValueError:

    print(f"Lo siento, el formato no es correcto")