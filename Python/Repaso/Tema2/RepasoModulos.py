'''
Created on 26 dec. 2018

@author: IvanPerez9

'''
import  random
import statistics

"""
Reimplementar la función que hacia uso de los apodos de un
héroe para mostrar un mensaje usando el módulo random.

NO VA A IR AQUI, ASI QUE LA PONGO EN REPASO SUPERHEROE -> noticia2
"""

#random.sample(lista, numero)

"""
Dadas propiedades inmobiliarias con tipo y precio, calcular la
media y mediana por tipo, número de viviendas por rango de
precios y moda de todas las propiedades
"""

tipo = {"apartamento" , "piso" , "casa" , "loft" , "rustico"}
propiedad = []
for i in range(10):
    propiedad.append((random.sample(tipo,1)[0] , random.randint(20000 , 300000)))

print(propiedad)

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

#Pongo solo 1 letra para hacelo más corto
def lanzarmoneda ():
    moneda = random.randint(0,1)
    if moneda == 0:
        return "H" #HEAD
    else:
        return "T" #TAIL

print(lanzarmoneda())

#Crear una función que, mientras no se de una secuencia de cara o cruz, siga tirando monedas.

def secuencia (seq):
    lanzamiento = lanzarmoneda()
    while seq not in lanzamiento:
        lanzamiento += lanzarmoneda()
    return lanzamiento

print(secuencia("HHT"))

#Modificar la función anterior para que reciba 2 secuencias de cara o
#cruz, y lance monedas hasta que una de las dos se cumpla.
#Cuando se cumpla devuelve la secuencia ganadora y los lanzamientos.

def secuenciaGanadora (seq1,seq2):
    lanzar = lanzarmoneda()
    numeroLanzamiento = 0
    while seq1 not in lanzar and seq2 not in lanzar:
        lanzar += lanzarmoneda()
        numeroLanzamiento += 1
    if lanzar in seq1:
        return print("Secuencia ganadora: " + seq1 + " lanzamientos: " + str(numeroLanzamiento))
    else:
        return print("Secuencia ganadora: " + seq2 + " lanzamientos: " + str(numeroLanzamiento))

secuenciaGanadora("TTH", "HTT")

#Crear una función que pida 2 secuencias y devuelva que
#secuencias gana 100 partidas la primera.

def win (seq1,seq2):
    lanzar = lanzarmoneda()
    while seq1 not in lanzar and seq2 not in lanzar:
        lanzar += lanzarmoneda()
    if lanzar in seq1:
        return seq1
    else:
        return seq2

def secuencia100 (seq1, seq2):
    ganadas1 = 0
    ganadas2 = 0
    for i in range(100):
        if win(seq1,seq2) == seq1 :
            ganadas1 += 1
        else:
            ganadas2 += 1

    if ganadas1>ganadas2 :
        return print("Gana " + seq1 + " con: " + str(ganadas1))
    else:
        return print("Gana " + seq2 + " con: " + str(ganadas2))

secuencia100("HTT" , "THT")