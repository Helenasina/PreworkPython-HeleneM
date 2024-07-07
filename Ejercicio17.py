'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.'''
def millas_a_kilometros(millas):
    conversion = 1.60934
    kilometros = millas * conversion
    return kilometros

try:
    millas = float(input("Ingrese la distancia en millas a convertir en Km: "))    
    kilometros = millas_a_kilometros(millas)
    print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros")
    
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

