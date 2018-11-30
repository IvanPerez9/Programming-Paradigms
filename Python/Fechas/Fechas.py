'''
Created on 28 nov. 2018

@author: Iván
'''
import datetime

"""
Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)
"""

f = datetime.date(2018,12,31)
print(f.strftime("%j"))

"""
Teoria sobre fechas:


"""