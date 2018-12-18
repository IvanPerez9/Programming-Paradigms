'''
Created on 18 dec. 2018

@author: Iván
'''
"""
SLICE

a[inicio:final:salto]
a[-2:]   # selecciona los dos últimos elementos del array
a[:-2]   # selecciona todos los elementos excepto los dos últimos

a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[start:end:step] # start through not past end, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

"""
# Slice
# Crear una función que devuelva el máximo y mínimo de 2 números.

def maxMin (n,m):
    if n < m :
        print(m)
    else:
        print(n)

maxMin (3,2)

#Crear un función que devuelva el máximo y mínimo de una lista de números.

def maxMinL (lista):
    print("El maximo de " + str(lista) + " es " + str(maximo(lista)))
    print("El minimo de " + str(lista) + " es " + str(minimo(lista)))

def maximo (lista):
    max = 0
    for i in range(0,len(lista)):
        if lista[i] > max :
            max = lista[i]
    return max

def minimo (lista):
    min = maximo(lista)
    for i in range(0,len(lista)):
        if lista[i] < min :
            min = lista[i]
    return min

l = [1,2,3,4,5,6]
maxMinL(l)

#
#Crea una función que recibe una cadena y la devuelve en sentido inverso.

def invertirCadena (cadena):
    return (cadena [::-1] )

print(invertirCadena("Hola"))

#– Crea una función que recibe una cadena y devuelve la misma
# cadena con sólo la primera letra mayúscula

def mayusCadena (cadena):
    return cadena [0:1].upper() + cadena [1:].lower()

print(mayusCadena("jejejeE"))

#Crea una función que imprima por pantalla una matriz (lista de listas).

matriz = [[1,2,3], [2,2,2]]

def imprimirMztriz (m):
    for i in range(len(m)+1):
        for j in range(len(m)):
            print(m[j][i], end =" ") #Para la misma linea

imprimirMztriz(matriz)

"""
Implementar las funciones:
apilar(pila, elemento)
desapilar(pila)
cima(pila)
"""

def apilar (pila, e):
    pila.append(e)
    return pila

def desapilar (pila):
    return pila.pop()

def cima (pila):
    return pila [-1]

"""
encolar(cola, elemento)
desencolar(cola)
primero(cola)
"""

def encolar (cola,e):
    cola.insert(0,e)
    return cola

def desencolar (cola):
    cola.pop()

def primero (cola):
    return cola [-1]

"""
Implementa un programa que devuelva si en una cadena que
recibe de entrada, los paréntesis que en ella aparecen están
balanceados.
"""

def balanceados (cadena):
    #Comprobar que todos cierran
    pila = []
    for i in cadena:
        if i == "(" :
            apilar(pila,i)
        elif i == ")":
            if len(pila) == 0: #Vacia
                print("No está balanceado")
                break
            else:
                desapilar(pila)
    if len(pila) == 0 :
        print("Está balanceado")
    else:
        print("Desbalanceado")

balanceados("Hola()() esto )()(")
balanceados("()/(")

# Reimplementar la función del calculo de los 100 primeros primos
# haciendo uso de conjuntos.

def cien ():
    c = set()
    for i in range(2,100):
        if isPrimo(i):
            c.add(i)
    return c

def isPrimo (n):
    if n < 0:
        return False
    elif n == 2 :
        return True
    else:
        for i in range(2,n):
            if n % i == 0 :
                return False
        return True

print(cien())

#Crear una función que recibe un número y devuelve una lista con sus dígitos

def digitos (num):
    aux = list()
    while num:
        aux.append(num % 10)
        num = num//10
    return aux

print(digitos(1234))

"""
CUBINFINITO
Un número es cubifinito si al elevar al cubo sus dígitos y
sumarlos da como resultado 1 u otro número cubifinito. Crear
una función que reciba un número y devuelva si es cubifinito
"""

#– Implementar las funciones sobre conjunto, unión, intersección, diferencia y copia.

def union (c1,c2):
    c3 = set()
    c3.union(c1)
    c3.union(c2)
    return c3

c1 = {1,2}
c2 = {3,4,5}
c3 = {3,4,7}
c4 = {1,2,3}
union(c1,c2)

def union2 (c1,c2):
    c = set()
    for e in c1 :
        c.add(e)
    for i in c2:
        c.add(i)
    return  c


def interseccion(c1, c2):
    c = set()
    for e in c1:
        for e in c2:
            c.add(e)

    return c

interseccion(c1,c4)

def diferencia (c1,c2):
    c = set()
    for i in c1:
        for i in not c2:
            c.add(i)

    return c


"""
En una lista hay números en parejas, positivos y negativos (si
está el 3, está el -3) pero en posiciones desconocidas. Todos los
números tienen su pareja de signo opuesto excepto uno. Crea
una función que dada una lista de este tipo, devuelva el
elemento desparejado.
"""


def opuestos(lista):
    suma = 0
    for e in lista:
        suma += e
    return suma


print(opuestos([1, -1, 2, 3, 4, -3, -2]))

#En una lista de números, todos están repetidos excepto uno.
#Crea una función que devuelva el número no repetido.

def repetidos(lista):
    vistos = set()
    for e in lista:
        if e not in vistos:
            vistos.add(e)
        elif e in vistos:
            vistos.remove(e)

    return vistos


print(repetidos([1, 2, 3, 4, 2, 3, 1]))

#Dado un conjunto de números, devolver una tupla con 2
#conjuntos, el primero contendrá los pares y el segundo los impares

def paresImpares (c):
    pares = set()
    impares = set()
    for i in c :
        if i%2 == 0:
            pares.add(i)
        else:
            impares.add(i)
    return pares,impares

print("Pares e impares: ")
print(paresImpares({1,2,3,4,5,6,7,8}))

#Crear una función que devuelva el conjunto potencia
#Es devolver la lista con subconjuntos de como se creo el conjunto dado

"""REPASAR"""

def addTo(e, t):
    for s in t:
        s += [e]
    return t


def conjunto_potencia(a_set):
    if not a_set: return [[]]
    e = a_set[0]
    t = a_set[1:]  # Todos menos el primero
    return conjunto_potencia(t) + addTo(e, conjunto_potencia(t))


print(conjunto_potencia([1, 2, 3, 4, 5]))

