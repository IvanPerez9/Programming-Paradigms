'''
Created on 18 nov. 2018

@author: ivan
'''
from _overlapped import NULL

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
    
print(cubifinito(1243, []))
         
    

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

