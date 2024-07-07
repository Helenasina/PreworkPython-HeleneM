'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''
def contar_palabras(oracion):
    # Dividir la oración en palabras utilizando el espacio como separador
    palabras = oracion.split()
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    return cantidad_palabras

try:
    oracion = input("Ingrese una oración: ")
    cantidad_palabras = contar_palabras(oracion)
    print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")
    
except ValueError:
    print("Lo siento, no ha ingresado valores numéricos válidos")

