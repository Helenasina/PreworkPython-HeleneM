'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario
'''

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b

def calcular():
    print("Seleccione la operación (1,2,3 o 4) que desea:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    eleccion = input("Operación a realizar numero: ")
    if eleccion == '1':
            print("Has elegido sumar")
            num1 = float(input("Ingrese un primer número: "))
            num2 = float(input("Ingrese el número a sumarle: "))
            print(f"La suma de {num1} y {num2} es: {suma(num1, num2)}")
    elif eleccion == '2':
            print("Has elegido restar")
            num1 = float(input("Ingrese un primer número: "))
            num2 = float(input("Ingrese el número a restarle: "))
            print(f"La resta de {num1} y {num2} es: {resta(num1, num2)}")
    elif eleccion == '3':
            print("Has elegido multiplicar")
            num1 = float(input("Ingrese un primer número: "))
            num2 = float(input("Ingrese el número por el cual multiplicarle: "))
            print(f"La multiplicación de {num1} y {num2} es: {multiplicacion(num1, num2)}")
    elif eleccion == '4':
            print("Has elegido dividir")
            num1 = float(input("Ingrese un primer número: "))
            num2 = float(input("Ingrese el número por el cual dividirle: "))
            if num2 == 0:
                print ("No se puede dividr por zero")
            else: print(f"La división de {num1} y {num2} es: {division(num1, num2)}")
    
    else:
        print("Lo siento, la opción seleccionada no es válida")

# Ejecutar el programa
calcular()

