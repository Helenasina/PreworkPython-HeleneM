'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
def contar_vocales(palabra):
    vocales = "aeiouy"
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador +=1
    return contador

# Pedir al usuario una palabra
palabra = input("Ingresa una palabra para saber cuantas vocales tiene: ")

# Contar vocales y almacenar el resultado el la variable 'suma'
suma = contar_vocales(palabra)

print(f"La palabra {palabra} contiene {suma} vocales.")

