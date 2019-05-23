
import random

"""
Implementar las funciones:
apilar(pila, elemento)
desapilar(pila)
cima(pila)
"""

def apilar (pila, elemento):
    pila.append(elemento)
    return pila

def desapilar (pila):
    pila.pop()
    return pila

def cima (pila):
    cima = pila.pop();
    return cima

def cima2 (pila):
    return pila[-1]

def encolar (cola, elemento):
    cola.insert(0, elemento)
    return cola

def desencolar (cola):
    cola.pop()
    return cola

def primero (cola):
    return cola.pop()

# Parentesis balanceados o no

def balanceados (cadena):
    list1 = list() # Como pilas
    mitad = False;
    for i in cadena:
        if i == '(' :
            apilar(list1, i)
        elif i == ')':
            if len(list1) == 0:
                mitad = True;
                break;
            desapilar(list1)

    if (len(list1) == 0) and ( mitad != True):
        print("Balanceados")
    else:
        print("No balanceados")

#balanceados("Hola ())")

#Sacar digitos de un numero

def digitos(num):
    l = list()
    for i in str(num):
        l.append(i)
    return l

#print(digitos(1234))

#Implementar las funciones sobre conjunto, union, interseccion y diferencia y copia

def union (c1,c2):
    c3 = c1 | c2 ;
    return c3

def interseccion (c1,c2):
    c3 = c1 & c2 ;
    return c3

def diferencia (c1,c2):
    return c1 - c2

"""
En una lista hay números en parejas, positivos y negativos (si
está el 3, está el -3) pero en posiciones desconocidas. Todos los
números tienen su pareja de signo opuesto excepto uno. Crea
una función que dada una lista de este tipo, devuelva el
elemento desparejado.
"""

def signoOpuesto (l):
    suma = 0;
    for i in l:
        suma += i;
    return suma

listaOpuestos = [1,2,-1,-2,3,-4,4]
print(signoOpuesto(listaOpuestos))

# En una lista estan todos los elementos repetidos menos uno, devuelve el no repetido

def noRepetido (l):
    visto = set()
    for i in l:
        if (i not in visto):
            visto.add(i)
        else:
            visto.remove(i)
    return visto

# Dado un conjunto de numeros devolver un conjunto con una tupla de pares y otra de impares

def paresImpares (c):
    pares = set();
    impares = set();
    for i in c:
        if (i % 2 == 0):
            pares.add(i)
        else:
            impares.add(i)
    return (pares , impares)

#conjuntoPI = {1,2,3,2,1,3,45,32,5}
#print(paresImpares(conjuntoPI))


"""
Crear una función que devuelva el conjunto cartesiano de dos
conjuntos (conjunto con todos los pares del primero con el
segundo).
"""

def cartesianos (c1,c2):
    c = set()
    for i in c1:
        for e in c2:
            c.add((e,i))
    return c

#print(cartesianos({1,2},{3,4,5}))

# Funcion que devuelva el numero de apariciones de cada caracter en una cadena

def caracter (s):
    d = dict();
    for c in s:
        if (c not in d):
            d[c] = 1
        else:
            d[c] += 1
    return d

#print(caracter("Hola que tal como estas"))

#Funcion que devuelva el numero de apariciones de una palabra en una frase

def palabraFrase (s):
    d = dict();
    palabras = s.upper().split(" ")
    for i in palabras:
        if (i not in d):
            d[i] = 1;
        else:
            d[i] += 1

    return d;

#print(palabraFrase("Hola que tal hola"))

#Simular N tiradas de dados y cuente las veces que aparece un resultado

def tirada (n):
    d = {2:0 , 3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    for i in range(n):
        random1 = random.randint(1,6)
        random2 = random.randint(1,6)
        d[random1+random2] += 1

    print(d)

# Funcion que devuelve el inverso de un diccionario

def inversoDic (d):
    k = d.keys();
    v = d.values();
    d1 = dict(zip(v,k))
    return d1