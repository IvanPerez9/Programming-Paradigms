'''
Created on 13 dec. 2018

@author: Iván
'''

import math

# Dada una altura pintar una piramide de asteriscos
from builtins import range

n = int(input("Introduce el numero de filas del triangulo: "))

for i in range(n):
    espacios = n-i;
    print(" " * espacios + "*" *(i*2+1))

# Pirámide invertida

n = int(input("Introduce el numero de filas del triangulo invertido: "))

for i in range(n-1 , -1 , -1):
    print(" " * (n-i) + "*" * (2*i+1))

# Pintar un rombo

nr = int(input("Tamaño del rombo: "))

def rombo (n):
    for i in range(n):
        print(" " * (n-i) + "*" * (2*i+1))
    for i in range(n-2 , -1 , -1):
        print(" " * (n-i) + "*" * (2*i+1))

rombo(nr)

#Factorial de un numero

fact = int(input("Introduce el numero del que quieres el factorial: "))

def factorial (n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(fact))

# Crear una funcion que resuelve una ecuacion de segundo grado recibiendo a, b, c

def ecuacionSegundo (a,b,c):
    ecuacion = (-b + math.sqrt(b**2 - (4 * a *c))) / (2*a)
    print(str(ecuacion))

a = int (input("Introduce el valor de a: "))
b = int (input("Introduce el valor de b: "))
c = int (input("Introduce el valor de c: "))
ecuacionSegundo(a, b, c)