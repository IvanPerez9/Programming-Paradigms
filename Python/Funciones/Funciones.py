
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
    print("El area es: " + str(areaA))
    
base = int(input("Introduces una base: "))
altura = int(input("Introduces una altura: "))
area(base, altura)

#Crear una funcion que devuelva el perimetro de una circunferencia (utilizando math).

def perimetro (radio):
    perime = 2 * math.pi * math.sqrt(radio)
    print("El perimetro es: " + str(perime))

radio = float (input("Introduce el radio de la circunferencia: "))
perimetro(radio)

# Crear una funcion que calcule el factorial de n

def factorial (n):
    if n == 0 :
        return  1
    else:
        return n * factorial(n-1)

n = int(input("Introduzca el valor n para factorial: "))
print(factorial(n))

# Crear una funcion que resuelve una ecuacion de segundo grado recibiendo a, b, c

def ecuacionSegundo (a,b,c):
    ecuacion = (-b + math.sqrt(b**2 - (4 * a *c))) / (2*a)
    print(str(ecuacion))

a = int (input("Introduce el valor de a: "))
b = int (input("Introduce el valor de b: "))
c = int (input("Introduce el valor de c: "))
ecuacionSegundo(a, b, c)
