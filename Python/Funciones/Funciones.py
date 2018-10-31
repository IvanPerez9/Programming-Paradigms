from math import pi
import math

# Sin valor de retorno, si devuelvo algo bien, sino pues nada sin return

def imprime(parametro):
    print(parametro)
    
imprime("Hola")
imprime(2)



# Tener el codigo documentado, ya que no tiene tipos y no sabe lo que se devuelve 

#Hacer funcion que dada una altura pinte un rombo

def rombo (altura):
    for i in range(n):
        print(' ' *(n-i) + '*' *(2*i+1))
    for i in range (n-2 ,-1 ,-1):
        print(" " * (n-i) + "*" * (2*i+1))

n = int (input("Introduce le numero de files del rombo: "))
rombo(n)

#Crear una funcion que devuelva el area de un rectangulo.

def area (base,altura):
    areaA = base*altura
    print("El area es: " + areaA)
    
base = int(input("Introduces una base: "))
altura = int(input("Introduces una altura: "))
area(base, altura)
