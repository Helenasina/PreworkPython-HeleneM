'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100
'''
def suma_numeros_pares():
    contador = 0
    for numero in range(1, 101):
        if numero % 2 == 0: #el modulo '%' devuelve el resto de la división entre dos números
            contador += numero
    return contador

# Calcular la suma de los números pares y almacenar el resultado el la variable 'resultado'
resultado = suma_numeros_pares()

print(f"La suma de los números pares de 1 a 100 es {resultado}")
