'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''
def contar_pares_impares(lista):
    pares = 0
    impares = 0 #inicializar los dos contadores a 0
    
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

try:
    entrada = input("Ingrese una lista de números separados por espacios: ")
    
    # se usa map(int, ...) para convertir cada string del input usuario en números enteros
    # y split() divide la entrada en una lista de cadenas basada en espacios
    lista_numeros = list(map(int, entrada.split()))
    
    # Llamar a la función para contar pares e impares
    cantidad_pares, cantidad_impares = contar_pares_impares(lista_numeros)

    print(f"Cantidad de números pares: {cantidad_pares}")
    print(f"Cantidad de números impares: {cantidad_impares}")

except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

