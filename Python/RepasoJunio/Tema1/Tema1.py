import math

# Dada una altura pintar una pirámide

def piramide ():
    altura = int(input("Introduce una altura: "))

    for i in range(altura):
        espacios = altura-i
        print(" " * espacios + (i*2+1) * "*")

#piramide()

#Pintar una piramide invertida

def piramideInvertida ():
    altura = int(input("Introduce una altura para la piramide invertida: "))

    for i in range(altura-1, -1 , -1): #Inicio, final y avance
        espacios = altura - i;
        print(" " * espacios + (i*2+1) * "*")

#piramideInvertida()

#Pintar un rombo

def printarRombo():
    tamano = int(input("Introduce el tamaño del rombo a pintar: "))

    for i in range(tamano):
        print(" " * (tamano-i) + (2*i+1) * "*")
    for i in range(tamano-2, -1, -1):
        print(" " * (tamano-i) + (2*i+1) * "*")

#printarRombo()

# El area de un rectangulo

def areaRectangulo ():
    base = int(input("Base del rectangulo: "))
    altura = int(input("Altura del recangulo: "))

    print(base * altura)

#areaRectangulo()

#Perimetro de una circunferencia utilizando math

def perimetroCircunferencia ():
    radio = int(input("Introduce el radio de la circunferencia: "))

    return 2 * math.pi * radio

#print(perimetroCircunferencia())

# Factorial de un numero dado

numeroFactorial = int(input("Introduce numero factorial: "))

def factorial (n):
    if n == 0:
        return 1
    elif n <= 2:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(numeroFactorial))

# Lista de numero primos en el rango 0-100

#Diapo 36