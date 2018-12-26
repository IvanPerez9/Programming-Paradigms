'''
Created on 28 nov. 2018

@author: Iván
'''
"""
Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)
"""

import datetime
import random


f = datetime.date(2018,12,31)
print(f.strftime("%j"))

"""
Crear la función inversa a la anterior
"""

g = datetime.datetime.strptime("365" , "%j")
print(g)

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
print("Ejercicio Paradoja cumpleaños: \n")


def fechaRandom ():
    random_date = random.randint(1, 365)
    return datetime.datetime.strptime(str(random_date), "%j")

    # Mio anterior
    #random_date = fechaini + (fechafin - fechaini) * random.random()
    #return random_date

print(fechaRandom())

def fechaGuardar2 ():
    s = set();
    d = fechaRandom();
    while d not in s:
        s.add(d)
        d = fechaRandom()
    return len(s) + 1 , s ,d

print(fechaGuardar2())

def fechaGuardar ():
    
    """
    Uso una lista para almacenar fechas
    """
    
    guardar = []
    coinciden = False
    
    while not coinciden :
        fecha = fechaRandom()
        if fecha not in guardar:
            guardar.append(fecha)
        else:
            #guardar.pop(fecha)
            coinciden = True
        
    return len(guardar)+1
    #return ("Coincide: " + fecha.str + "y ha calculado: " + str(len(guardar)))

print("Ha calculado: " + str(fechaGuardar()))

def fechaPersonas(n):
    suma = 0;
    media = 0;
    """
    Si me vienen en una tupla, puedes poner variables con comas 
    a,b,c = fechaGuardar2()
    si no usas b y c , puedes poner a,_,_ 
    
    O puedes usar indices de tuplas,  suma += suma + fechasGuardar2() [0] 
    """
    for i in range(n):
        suma += fechaGuardar()
    
    media = suma / n 
    return media
        
print("De media: " + str(fechaPersonas(10)))

# ahora.strftime(“%d-%m-%y. %d %b %y. %A, %d %B %Y.”)
# Dia mes y año , pero en distintos formatos. Formato corto, uno más largo