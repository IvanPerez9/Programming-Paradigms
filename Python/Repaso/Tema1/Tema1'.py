'''
Created on 18 dec. 2018

@author: Iván
'''
import random
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

def union (c1,c2): # | union
    c3 = c1 | c2
    return c3

c1 = {1,2}
c2 = {3,4,5}
c3 = {3,4,7}
c4 = {1,2,3}
print(union(c1,c2))

def union2 (c1,c2):
    c = set()
    for e in c1 :
        c.add(e)
    for i in c2:
        c.add(i)
    return  c

print(union2(c1,c2))

def interseccion(c1, c2): #Interseccion
    c = c1 & c2
    return c

print("Interseccion" + str(interseccion(c1,c4)))

def diferencia (c1,c2):
    c = set()
    for i in c1:
        for i in not c2:
            c.add(i)
    return c

def diferencia2(c1, c2): #Interseccion
    c = c1 - c2
    return c

#print("Diferencia" + str(diferencia(c3,c2)))
print("Diferencia2" + str(diferencia2(c3,c2)))


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

#Si hay más de 1 sin opuesto, con un set de "vistos"

def opositePair(l):
    c = set()
    for e in l:
        if e not in c:
            c.add(-e)
        else:
            c.remove(e)
    return c

print(opositePair([1, -1, 2, 3, 4, -3, -2]))
print(opositePair([1,-1,2,-2,1,3]))
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

"""
Crear una función que devuelva el conjunto cartesiano de dos
conjuntos (conjunto con todos los pares del primero con el
segundo).
"""
print("Cartesianos")
def cartesianos (c1,c2):
    c = set()
    for i in c1:
        for e in c2:
            c.add((e,i))
    return c

print(cartesianos({1,2},{3,4,5}))

#– Crear una función que devuelva el número de apariciones de
# cada carácter en una cadena.

#Añadir al diccionario con C

def characters(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1 # Clave c con valor 1
        else:
            d[c] += 1
    return d

print(characters("HolaaaS"))

#Crear una función que devuelva el número de apariciones de cada palabra en una frase

def cuentaPalabras (cadena):
    d = dict()
    palabras = cadena.split()
    for i in palabras:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(cuentaPalabras("Hola que tal estás que"))

#– Utilizando el modulo random, crear una función que simule N
# tiradas de 2 dados y cuente las veces que aparece un resultado.

def tiradas (n):
    d = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0} #Clave valor de todos los posibles valores
    for i in range(n):
        random1 = random.randint(1,6)
        random2 = random.randint(1,6)
        d[random1+random2] += 1 
        #Acceso a la clave del diccionario directamente
    print(d)
    

tiradas(5)

#Reimplementacion de contar caracteres con get

def contarReimplementado (c):
    d = dict()
    for i in c:
        d[c] = d.get(c,0) + 1 #La clave y el default si no la encuentra (0)
    return d

print(contarReimplementado("Holaaa"))

#Crear una función que devuelva el diccionario inverso.

def inversoDic (dic):
    k = dic.keys()
    v = dic.values()
    d = dict(zip(v,k))
    return d

d = {"Uno" : 1, "Dos" :2 , "Tres":3}
print(inversoDic(d))

#Crear una función que gestione una agenda, permitirá agregar
#números de teléfono a personas.

agenda = {"Pepe" : 123 , "Maria" : 456}

def agregar (t,n,agenda):
    if n not in agenda.keys():
        agenda[n] = t
    else:
        agenda[n] = agenda.get(n,set(t))

print(agenda)
agregar(128,"Ivan" , agenda)
print(agenda)

def eliminar (n,agenda):
    if n in agenda.keys():
        agenda.pop(n)

eliminar("Ivan" , agenda)
print(agenda)

# Crear una función que escribe una cadena en Morse.


def morseTraduccion (cadena):
    morse = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.',
             'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..',
             '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
             '!': '--..--'}
    traducido = []
    palabras = cadena.split()
    for e in palabras:
        traducido.append(morse.get(e))
        traducido.append(" ")

    cadena1 = ''.join(str(traducido))
    print(traducido)
    print(str(cadena1))


print(morseTraduccion("HOLA QUE TAL"))