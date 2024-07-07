'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def es_palindromo(palabra):

    # Comparar la palabra de izquierda a derecha y de derecha a izquierda
    return palabra == palabra[::-1]

# Pedir al usuario que ingrese una palabra
palabra = input("Ingresa una palabra para saber si es un palidromo: ")

if es_palindromo(palabra):
    print(f"Efectivamente,'{palabra}' es un palíndromo!")
else:
    print(f"Lo siento,'{palabra}' no es un palíndromo.")
