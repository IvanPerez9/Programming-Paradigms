import datetime
import random

"""
Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)
"""

def juliano (fecha):
    print(fecha.strftime("%j"))

d = datetime.date(2018,5,30)
juliano(d)

"""
Crear la función inversa a la anterior
"""

def gregoriano (fecha):
    print(fecha.strptime("365" , "%j"))

