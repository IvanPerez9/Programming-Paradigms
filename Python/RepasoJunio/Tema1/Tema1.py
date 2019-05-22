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

#numeroFactorial = int(input("Introduce numero factorial: "))

def factorial (n):
    if n == 0:
        return 1
    elif n <= 2:
        return n
    else:
        return n * factorial(n - 1)

#print(factorial(numeroFactorial))

# Lista de numero primos en el rango 0-100

#Diapo 36

def esPrimo(n):
    if (n < 0):
        return False
    elif (n == 2):
        return True
    else:
        for i in range(2, 100):
            if (n % i == 0):
                return False
            else:
                return True

def primosLista():
    l = list()
    for i in range(1,100):
        if esPrimo(i):
            l.append(i)

    return l;

#print(primosLista())

#Dada una lista imprimir los elementos en posicion par

listaPar = [1,2,3,4,5,6,7,8,9,10,2,2,2,2,2]

def imprimirPar(listaPar):
    for i in range(0,len(listaPar), 2):
        if(i % 2 == 0):
            print(listaPar[i])

#imprimirPar(listaPar)

#Crear una función que recibe una lista de números y devuelve
#una lista de tuplas por cada elemento. Cada tupla tendrá el
#elemento, su cuadrado y su cubo:

def imprimirTuplas (l):
    listaAux = list()
    for i in l:
        tupla = (i , i**2 , i**3)
        listaAux.append(tupla)

    return listaAux

listaTuplas = [1,2,3,4,5,6,7]
#print(imprimirTuplas(listaTuplas))

#Funcion que devuelva el maximo y el minimo de una lista

def maximoLista (l):
    maximo = 0
    for i in l:
        if (maximo < i):
            maximo = i;
    return maximo

def minimoLista (l):
    minimo = maximoLista(l)
    for i in l:
        if (minimo > i):
            minimo = i;
    return minimo

listaM = [1,2,3,5464,7658,56843,235568,7]
#print("El maximo de la lista es: " + str(maximoLista(listaM)))
#print("El minimo de la lista es: " + str(minimoLista(listaM)))

#Funcion que recive una cadena y la devuelve en sentido inverto -> Slice

def cadenaInversa ():
    cadena = "Hola que tal"
    return cadena[::-1]

#print(cadenaInversa())

#Imprimir primera mayuscula

def mayus ():
    cadena = "hola que"
    print(cadena[0:1].upper() + cadena[1::].lower())

#mayus()

#Imprimir una matriz

