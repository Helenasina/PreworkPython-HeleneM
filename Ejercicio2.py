'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''
def Cuenta(lista):
    Cuenta = 0 #inicializar los dos contadores a 0
    for Plato in lista:
        Cuenta += Plato
    return round(Cuenta * 1.15, 2)

lista = [12, 14, 11.5, 13, 12.5]

print(Cuenta(lista))

