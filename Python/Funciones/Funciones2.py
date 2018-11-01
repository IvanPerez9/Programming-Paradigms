'''
Created on 31 oct. 2018

@author: Ivan
'''
import math


#Modificar el ejercercicio que calcula una ecuacion de segundo grado para que utilice parametros por defectos = 0
def ecuacionSegundo (a=0,b=0,c=0):
    try:
        ecuacion = (-b + math.sqrt(b**2 - (4 * a *c))) / (2*a)  
        ecuacion2 = (-b - math.sqrt(b**2 - (4 * a *c))) / (2*a)
        print(str(ecuacion)++ "y" ++ str(ecuacion2))
    except ValueError:
        print("No hay solucion real")

a = int (input("Introduce el valor de a: "))
b = int (input("Introduce el valor de b: "))
c = int (input("Introduce el valor de c: "))
ecuacionSegundo(a, b, c)