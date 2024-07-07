'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''
def convertir_minutos_a_horas_y_minutos(minutos):
    horas = minutos // 60 #la division dara una cifra entera
    minutos_restantes = minutos % 60 #el modulo '%' devuelve el resto de la división entre dos números
    return horas, minutos_restantes

try:
    minutos = int(input("Ingrese el número de minutos a convertir: "))
    
    if minutos < 0:
        print("Error: El número de minutos debe ser mayor o igual a cero.")
    else:
        horas, minutos_restantes = convertir_minutos_a_horas_y_minutos(minutos)
        print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")
