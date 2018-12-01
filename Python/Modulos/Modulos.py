'''
Created on 28 nov. 2018

@author: Iván
'''

"""
– Reimplementar la función que hacia uso de los apodos de un
héroe para mostrar un mensaje usando el módulo random
"""
#def noticia (superheroe): DE LA CLASE SUPERHEROE
"""
Dadas propiedades inmobiliarias con tipo y precio, calcular la
media y mediana por tipo, número de viviendas por rango de
precios y moda de todas las propiedades.
"""
#Si tienes un tipo y un valor, casi seguro un diccionario

import random
import statistics


names = {"piso" , "local" , "rustico" , "edificable"} 
prop = []
for i in range (100):
    prop.append(((random.sample(names, 1)[0]), random.randint(2000, 100000)))

print(prop)

#l = list()
#d = dict(zip(list(names), l)) # Hacer un diccionario con la lista de nombres, y lista vacio 
#for p in prop:
#    d[p[0]].append(p[1])
    
#for k,v in d.items():
#    print(k + ": ", statistics.mean(v))
    
"""
Estafa cara o cruz:
• Crear una función que simule el lanzamiento de una moneda.
• Crear una función que, mientras no se de una secuencia de cara o
cruz, siga tirando monedas.
• Modificar la función anterior para que reciba 2 secuencias de cara o
cruz, y lance monedas hasta que una de las dos se cumpla.
Cuando se cumpla devuelve la secuencia ganadora y los
lanzamientos.
• Crear una función que pida 2 secuencias y devuelva que
secuencias gana 100 partidas la primera.
"""

def lanzar():
    if random.randint(0,1):
        return "H"
    else:
        return "T"
    
def match (seq):
    s = lanzar()
    while seq not in s:
        s += lanzar()
    return s
print(match("HTTH"))

def win (seq1, seq2):
    s = lanzar()
    while seq1 not in s and seq2 not in s:
        s += lanzar()
    return seq1 in s  #Cierto si seq1 está s. Devuelve una tupla (seq in s , s)

print(win("HTTH" , "HTT"))

def win2 (seq1,seq2):
    a,b = 0 , 0
    for i in range(100):
        if win(seq1,seq2):
            a += 1
        else:
            b +=1
    return a,b


s1 = "HHT"
s2 = "THT"

a,b = win2(s1, s2)

if a>b:
    print ("ha ganado" , s1 , a)
else:
    print("ha ganado" , s2 , b)
    
"""
La estafa consiste en poner siempre XYZ como -YXZ 
"""