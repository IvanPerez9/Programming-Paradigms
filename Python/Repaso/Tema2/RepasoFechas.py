'''
Created on 26 dec. 2018

@author: IvanPerez9
'''

import random
import datetime

"""
Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)
"""

def cambioF (fecha):
    print(fecha.strftime("%j"))

d = datetime.date(2018,12,31)
cambioF(d)

"""
Crear la función inversa a la anterior
"""

def cambioF2 (fecha):
    print(fecha.strptime("365" , "%j"))

"""
Paradoja del cumpleaños:
• ¿Cuántas personas tiene que haber en una habitación para que 2
de ellas cumplan los años el mismo día?
• Crear una función que devuelva una fecha aleatoria (mes y día)?
• Crear una función que guarda fechas aleatorias hasta que dos
coincidan (en mes y día) guardando cuantas ha generado.
• Crear una función que repite el experimento anterior N veces. De
media, ¿cuántas personas tiene que haber en la habitación para
que al menos 2 cumplan años el mismo día?
"""

def fechaAleatoria ():
    random_date = random.randint(1, 365)
    return datetime.datetime.strptime(str(random_date), "%j")

print(fechaAleatoria())

def guardarCoinciden ():
    cuantas = 0
    lista = list() #[]
    fechaA = fechaAleatoria()
    while fehcaA not in lista:
        cuantas += 1
        lista.append(fechaA)
        fechaA = fechaAleatoria()
    return fechaA , cuantas
    
prueba = guardarCoinciden()
print("La fecha: " + str(prueba[0]) + " coincide, y ha guardado: " + str(prueba[1]))

#Se repita N veces

def guardarNveces (n):
    contador = 0
    suma = 0
    while contador < n :
        interno = guardarCoinciden()
        suma += interno[1]
        contadoe += 1
    return (suma // contador)

print("De media se necesitan: " + str(guardarNveces(10)))
        


