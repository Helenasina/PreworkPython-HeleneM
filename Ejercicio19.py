'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no 
Nota : Un año es bisiesto si es divisible entre 4, sin embargo, si un año es divisible entre 100, 
entonces no es bisiesto, a menos que también sea divisible entre 400'''
def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
        #verifica si el año es divisible entre 4 pero no entre 100, o que el año es divisible entre 400
        return True
    else:
        return False

try:
    ano = int(input("Ingrese un año para verificar si es bisiesto: "))
    if es_bisiesto(ano):
        print(f"{ano} es un año bisiesto.")
    else:
        print(f"{ano} no es un año bisiesto.")
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

