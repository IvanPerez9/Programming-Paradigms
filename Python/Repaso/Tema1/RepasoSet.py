'''
Created on 18 nov. 2018

@author: ivan
'''


"""

Sets: Coleccion desordenada y mutable de objetos haseables (Convertir por hash)

     Hacer un set con las llaves {} , el set vacio tiene que ser con el constructor set() -> sino es un diccionario
     Soporta longitud consulta e iteracion... para modificar se usa add pop remove 

"""

# Reimplementar  la funcion de los 100 primeros primos haciendo uso de conjuntos
# Voy guardando los primo en un set

def cienPrimeros ():
    aux = set()
    for i in range(2,100):
        if isPrimo(i, aux):
            aux.add(i)
    return aux

def isPrimo (num,p):
    for e in p:
        if num % e == 0:
            return False
    return True

print(cienPrimeros())


# Crear una funcion que recibe un nuimero y devuelve una lista con suis digitos
# Mientras exista numero voy haciendo mod

def digitos (num):
    lista = []
    while num :
        lista.insert(0, num%10)
        num = num // 10
    return lista

print(digitos(12345))


#Cubifinito : Un numero es cubiinfinito si al elevar al cubo sus digitos y sumarlos da como resultado 1 u 
#                otro numero cubinfinito.

"""
TODO: ARREGLAR
"""
def cubifinito (num, aux = set()):
    
    conjuntoCubo = {1} # El uno es cubifinito,set
    l = digitos(num)

    suma = 0
    
    for e in l:
        suma += e** 3
    if suma in conjuntoCubo :
        return True
    elif suma == 1 :
        conjuntoCubo.add(num)
        cubifinito(num, aux) #Recursivo
    else:
        return False
    
print(cubifinito(10, []))
         
    

#Implementar las funciones sobre conjunto, union, interseccion, diferencia y copia.

def union (c1,c2):
    c = set()
    for e in c1 :
        c.add(e)
    for i in c2:
        c.add(i)
    return  c

def interseccion (c1,c2):
    c = set()
    for e in c1:
        for e in c2:
            c.add(e)
    
    return c

def diferencia (c1,c2):
    c = set()
    for e in c1:
        for e in not c2: #Not in 
            c.add(e)
    return c


def copia (c1):
    c = set()
    for e in c1:
        c.add(e)
    return c


"""

Los forcesets son set inmutables. Comparacion con issubset() e issuperset() , como poner < > 

"""

# Le paso una lista de parejas de positivos y negativos, todos tienen pareja menos 1 , encontrar y devolver cual es


def opuestos (lista):
    suma = 0
    for e in lista:
        suma += e
    return suma

print(opuestos([1,-1,2,3,4,-3,-2]))

    
def repetidos (lista):
    vistos = set()
    for e in lista:
        if e not in vistos:
            vistos.add(e)
        elif e in vistos:
            vistos.remove(e)
    
    return vistos

print(repetidos([1,2,3,4,2,3,1]))

"""
Lo mismo pero con un XOR , es un OR pero eliminando repetidos. Ver tabla de verdad
"""

def single (l):
    s = 0
    for e in l:
        s ^= e # ^ XOR 
    return s

print(single([1,2,3,4,2,3,1]))


def tuplaPares (conjunto):
    pares = set()
    impares= set()
    for e in conjunto:
        if e % 2 == 0:
            pares.add(e)
        else:
            impares.add(e)
    return pares,impares # Ojo como devolver la tupla

print(tuplaPares([1,2,3,4,5,6,7,8]))

#Conjunto potencia. Es devolver la lista con subconjuntos de como se creo el conjunto dado

def addTo(e, t):       
    for s in t:
        s += [e]
    return t
 
def conjunto_potencia(a_set):
        if not a_set: return [[]]
        e = a_set[0]
        t = a_set[1:] #Todos menos el primero
        return conjunto_potencia(t) + addTo(e, conjunto_potencia(t))
    
print(conjunto_potencia([1,2,3,4,5]))

"""
SLICE


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