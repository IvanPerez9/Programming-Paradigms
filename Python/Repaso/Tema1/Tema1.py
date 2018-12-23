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

#Crear una función que devuelva el área de un rectángulo.

a = int(input("Introduce la base del rectangulo: "))
b = int(input("Introduce la altura del rectangulo: "))

def areaR (a,b):
    return a*b

print(areaR(a,b))

#– Crear una función que devuelva el perímetro de una circunferencia (utilizando math).

radio = int(input("Introduce el radio de la circunferencia: "))

def perimetro (r):
    return 2*math.pi*r

print(perimetro(radio))

#Factorial de un numero

fact = int(input("Introduce el numero del que quieres el factorial: "))

def factorial (n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(fact))

# Crear una funcion que resuelve una ecuacion de segundo grado recibiendo a, b, c
# B^2 +- 4ac / 2a raiz

def ecuacionSegundo (a,b,c):
    x = ((b**2 - (4 * a *c)))
    if x<0 :
        return print("No hay solucion, factores dentro de la raiz menores que 0")
    elif x == 0:
        solucion = (-b) / (2*a)
        print(solucion)
    else:
        solucion1 = ((b) - math.sqrt(x) ) / (2*a)
        solucion2 = ((b) + math.sqrt(x) ) / (2*a)
        print("Solucion 1: " + str(solucion1))
        print("Solucion 2: " + str(solucion2))

a = int (input("Introduce el valor de a: "))
b = int (input("Introduce el valor de b: "))
c = int (input("Introduce el valor de c: "))
ecuacionSegundo(a, b, c)

#Crear una función que devuelva una lista con los números primos de 0 a 100.

def isPrime (n):
    if n < 0 :
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def primosLista ():
    l =  []
    for i in range(2,100):
        if isPrime(i):
            l.append(i)

    return l

print(primosLista())


#Dada una lista, imprimir los elementos en posición par.

def paresLista (l):
    for i in range(0,len(l), 2):
        print("Posicion par " + str(i) + ": " + str(l[i]))

lista = [0,4,67,34,55,2,8,10]
paresLista(lista)

#Un número es perfecto si la suma de sus divisores es igual a si
#mismo, ejemplo el 28. Crear una función que devuelva si un
#número es perfecto.

def divisores (num):
    listaDiv = []
    for i in range(1,num): #Ojo que empezar en 1
        if ((num % i) == 0):
            listaDiv.append(i)
    return listaDiv


def perfecto (num):
    """
    Comprueba si el numero es perfecto
    :param num: numero que comprobar
    :return: Perfecto o no
    """
    listaAux = divisores(num)
    suma = 0
    for i in range(len(listaAux)):
        suma += listaAux[i]
    if (suma == num) :
        return print("Es perfecto")
    else:
        return print("No es perfecto")


perf = int(input("Introduzca el numero que desea comprobar si es perfecto: "))
perfecto(perf)

#Crear una función que recibe una lista de números y devuelve
#una lista de tuplas por cada elemento. Cada tupla tendrá el
#elemento, su cuadrado y su cubo:

def listaTuplas (listaN):
    listaF = []
    for i in listaN:
        tupla = (i , i**2 , i*i*i)
        listaF.append(tupla)
    print(listaF)

lista2 = [1,2,3]
listaTuplas(lista2)

# Hasta Slyce