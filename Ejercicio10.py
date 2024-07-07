'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''
def determinar_dia(numero):
    dias_de_la_semana = {1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
    
    return dias_de_la_semana.get(numero, "Lo siento el número no es valido")
'''La función get de un diccionario se utiliza para obtener el valor correspondiente a una clave. 
Tiene la siguiente sintaxis: diccionario.get(clave, valor_por_defecto)
Donde clave es la clave que se busca en el diccionario y valor_por_defecto es el valor que se devuelve si la clave no se encuentra en el diccionario.'''

numero = int(input("Ingrese el número del dia de la semana (del 1 al 7): "))
#almacenar el resultado en la variable 'dia'
dia = determinar_dia(numero)

print(f"El dia correspondiente al número {numero} es: {dia}")

