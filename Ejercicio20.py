'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario'''
def sumar_lista(lista):
    suma = 0 #inicializar la variable en 0
    for numero in lista:
        suma += numero
    return suma

try:
    lista_usuario = input("Ingrese una lista de números separados por espacios: ")
    
    # se usa map(int, ...) para convertir cada string del input usuario en números enteros
    # y split() divide la entrada en una lista de cadenas basada en espacios
    lista_numeros = list(map(int, lista_usuario.split()))
    
    resultado = sumar_lista(lista_numeros)
    print(f"La suma de los números en la lista es: {resultado}")
    
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")