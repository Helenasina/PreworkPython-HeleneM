'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''

# Se importa el modulo datetime para trabajar con fechas y horas
from datetime import datetime
fecha_nacimiento_str = input("Ingrese su fecha de nacimiento en formato DD/MM/YYYY: ")

# Y se intenta convertir la fecha de nacimiento a un objeto datetime, si el formato da error se muestra mensaje
try:
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

    fecha_actual = datetime.now()

    edad = (fecha_actual - fecha_nacimiento).days // 365

    print(f"Tienes {edad} años.")
except ValueError:

    print(f"Lo siento, el formato no es correcto")    

