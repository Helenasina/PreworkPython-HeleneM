'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
'''

# Pedir al usuario una palabra y convertir su respuesta string en numero entero int()
Edad = int(input("Ingrese su edad: ")) 

if Edad < 18:
    print("El usuario no es mayor de edad")
else: print("El usuario es mayor de edad")


