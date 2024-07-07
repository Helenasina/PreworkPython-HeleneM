'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no (es decir si el número tiene divisores diferentes de 1 y él mismo)'''
def es_primo(numero):
    if numero <= 1:
        return False
    '''el operador '**' devuelve la raiz cuadrada. Verificar la divisibilidad hasta la raíz cuadrada,  
    en lugar del número completo, es una estrategia eficiente para determinar si un número es primo. 
    Permite reducir el número de pruebas necesarias y optimizar el tiempo de ejecución del algoritmo'''
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0: #el modulo '%' devuelve el resto de la división entre dos números
            return False
    return True

try:
    num = int(input("Ingrese un número entero positivo mayor que 1: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

