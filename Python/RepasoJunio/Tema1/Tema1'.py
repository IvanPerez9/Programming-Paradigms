import math
# Pintar piramide

n = int(input("Introduce una altura "))
for i in range(n):
    espacios = n - i
    print(" " * espacios + "*" * (i*2+1))

# Piramide invertira
print("-")

for i in range(n-1 , -1 , -1):
    espacios = n - i
    print(" " * espacios + "*" * (i*2+1))

#Rombo -> juntar los dos fors

#Perimetro de un circunferencia usando math

def perimetroCircunferencia (radio):
    print(2 * math.pi * radio)

# Resolver la ecuacion de segundo grado a,b,c

def ecuacion (a,b,c):
    x = ((b**2 - (4*a*c)))
    if x < 0 :
        print("No hay solucion")
    elif x == 0:
        sol = (-b) / 2*a
        print(sol)
    else:
        print("Solucion 1 " + (-b + x) / 2*a)
        print("Solucion 2 " + (-b) - x) / 2*a

# Funcion que de el facturial de un numero

def factorial (n):
    if (n == 0):
        return 1
    else:
        return n* factorial(n-1)

# Devolver lor 100 primeros primos

def esPrimo (n):
    if n< 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

def cienPrimos ():
    l = []
    for i in range(0,100):
        if esPrimo(i):
            l.append(i)
    print(l)

# Imprimir los elementos en posicion par de la lista

l = [1,3,5,7,8,9,0]

def imprimirPosPar(l):
    for i in range(len(l)):
        if i%2 == 0:
            print(l[i])

# Funcion que devuelve si un numero es perfecto -> La suma de sus divisores es igual a si mismo

def divisores(n):
    lista = list()
    for i in range(1,n):
        if (n % i) == 0:
            lista.append(i)
    return lista

def numeroPerfecto(n):
    l = divisores(n)
    suma = 0
    for i in l:
        suma += i
    if (suma == n):
        print("Es perfecto")
    else:
        print("No es perfecto")

# Devolver lista de tuplas con elemento, cuadrado y cubo

def listaTuplas (lista):
    listaSalida = list()
    for i in lista:
        aux = (i , i**2 , i**3)
        listaSalida.append(aux)
    return listaSalida


# Funcion que devuelva el maximo y el minimo de una lista

def maxMinL (l):
    print("Maximo: " + str(maximoL(l)))
    print("Minimo: " + str(minimoL(l)))


def maximoL (lista):
    maximo = 0;
    for i in lista:
        if i > maximo :
            maximo = i
    return maximo

def minimoL (lista):
    minimo = maximoL(lista)
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo

#maxMinL(l)
#print(max(l))

#Funcion que devuelve una cadena y la devuelve en sentido inverso

def invertirCadena (cadena):
    for i in range(len(cadena)-1 , -1 , -1):
        print(cadena[i] , end="")

invertirCadena("Hola")

def invertirCadena2 (cadena):
    print(cadena[::-1])

invertirCadena2("Hola")

# Devolver la misma cadena pero con la primera letra en mayuscula

def mayusPrimera (cadena):
    print(cadena[0].upper() + cadena[1:].lower())

mayusPrimera("ghola")

#Funcion que imprima una matriz -> Lista de listas

def matriz (m):
    for i in range(len(m)+1):
        for e in range(len(m)):
            print(m[e][i], end=" ")

ma = [[1,2,3], [3,3,3]]
matriz(ma)

#Implementar funciones de pilas y colas

def apilar (pila, elemento):
    pila.append(elemento)
    return pila

def desapilar (pila):
    return pila.pop()

def cima (pila):
    return pila[-1]

def encolar (cola, elemento):
    cola.insert(0,elemento) # Mejor con deque
    return cola

def desencolar (cola):
    cola.pop()

def primero (cola):
    return cola[-1]

# Implementar si los parentesis que recibe de una cadena estan o no balanceados

def balanceados (cadena):
    pila = []
    for i in cadena:
        if i == "(":
            apilar(pila,i)
        elif i == ")":
            if len(pila) == 0: #Vacia
                print("No balanceado")
                break;
            else:
                desapilar(pila)
    if (len(pila) == 0):
        print("Balanceados")
    else:
        print("No balanceados")

# 100 primeros primos pero con set

def cien ():
    c = set()
    for i in range(2,100):
        if esPrimo(i):
            c.add(i)
    return c

# Recibir un numero y devuelva una lista con sus digitos

def digitos (n):
    l = list();
    while n:
        l.append(n % 10)
        n = n // 10
    return l

# Cubinfinito -> Si al elevar al cubo sus digitos y sumarlos da como resultado 1 u otro cubinfinito
#Mirar

def cubinfinito (n):
    resultado = sum([int(x)**3 for x in str(n)])
    if resultado == 1:
        return True
    elif sum([int(x)**3 for x in str(resultado)]):
        return True
    else:
        return False
    return resultado == 1 or cubinfinito(resultado) == 1

print("-")
#Las veces que hay que iterar para alcanzar multiplicando digitos, un numero de 1 sola cifra

def persistence (num):
    contador = 0
    aux = 1
    if num > 10:
        for i in str(num):
            aux = aux * int(i)
            contador += 1

    return 1 + contador


print(persistence(123))

#Implementar las funcion sobre conjunto de union, interseccion, diferencia y copia

def union (c1,c2):
    c3  = c1.union(c2) # con | vale
    return c3

c1 = {1,2}
c2 = {2,3}

#Interseccion con & , diferencia con - , copia con :: en listas, aqui copy

def copia (c1,c2):
    c1 = c2.copy()
    return c1

print(str(copia(c1,c2)))

# Lista de numeros todos repetidos menos 1, devolver el no repetido

def noRepetido (l):
    visto = set()
    for i in l:
        if (i not in visto):
            visto.add(i)
        else:
            visto.remove(i)
    return visto

lista = {1,1,2,3,3,4,4,6,7,6,8,7}


#Devolver una funcion con el numero de apariciones de cada caracter de una cadena

def numApariciones (cadena):
    dic = dict();
    for i in cadena:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

print(numApariciones("Hola que tal como"))

# Numero de apariciones de palabras en una frase

def numAparicionesPalabras (frase):
    d = dict();
    palabras = frase.split()
    for i in palabras:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(numAparicionesPalabras("Hola hola que que tal"))

#Inverso del diccionario

def dicInverso (dic):
    keys = dic.keys()
    values = dic.values()
    dAux = dict(zip(values, keys))
    return dAux

d = {"Uno":1 , "Dos" :2 }
print(dicInverso(d))