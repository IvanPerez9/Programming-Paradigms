'''
Created on 31 oct. 2018

@author: Ivan
'''

#Dada una lista imprimir los elementos que esten en posicion par

lista = [0,1,2,3,4,5,6,7,8,9,10]

def pares (lista):
    for i in range(0,len(lista),2):
        print(lista[i])
    
pares(list(range(10)))
pares(lista)

#Funcion que de los numero primos del 1 al N , siendo N < 100

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  

def primos (n):
    if n < 100:
        print("Del 2 al " + str(n))
        print()
        for i in range(2,n):
            if (isPrime(i)): 
                print("El numero " + str(i) + " es primo")
    else:
        return print("El numero no puede superar el 100")
            
n = int(input("Introduzca hasta donde quiere ver si son primos: "))
primos(n)

#Un numero es perfecto si la suma de sus divisores es igual a si
#mismo, ejemplo el 28. Crear una funcion que devuelva si un numero es perfecto.

listaDiv = []

def divisores(num):
    for i in range(1,num):
        if ((num%i) == 0) :
            return lista.append(i)

def perfecto (num):
    divisores(num)
    global suma
    for i in range (len(listaDiv)):
        suma = suma + listaDiv[i];
        print(listaDiv[i])
    
    print("La suma de los divisores de " + str(num) + " es: " + str(suma))

num = int(input("Introduzca el posible numero perfecto: "))
perfecto(num)
