'''
Created on 14 nov. 2018

@author: Iván
'''
import random

# Collecion de parejas clave valor 
# Va entre llaves, constructor Dict es como poner el diccionario vacio {}
# Por eso el set vacio es con Set()
# Iterar en un diccionario con k y v (Klave y valor) 


# Funcion dado un conjunto devuelva su conjunto cartesiano

def cartesianos (c1,c2):
    c = set()
    for e1 in c1:
        for e2 in c2:
            c.add((e1,e2))
    return c 

print(cartesianos([1,2],[3,4,5,6]))

# Numero de apariciones de cada caracter en una cadena
cadena = "String"

def characters(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1 # Clave c con valor 1
        else:
            d[c] += 1
    return d

def dice2 (n):
    d = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    for i in range(n):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        d [a+b] += 1
        
    print (d)
    #NOOOPIPOHAMUERTO
dice2(9)