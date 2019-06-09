import datetime

"""
Crear una función que reciba una fecha (calendario gregoriano)
y devuelva el número de días desde el principio del año
(calendario juliano)
"""

def calendarioJuliano (fecha):
    print(fecha.strftime("%j"))

f = datetime.datetime.today()
f2 = datetime.date(2018,12,12)
calendarioJuliano(f2)
calendarioJuliano(f)

"""
Crear la función inversa a la anterior
"""

def calendarioGregoriano (fecha):
    print(fecha.strptime("365" , "%j").date())

date_str = '09-19-2018'

date_object = datetime.datetime.strptime(date_str, '%m-%d-%Y').date()
print(date_object)

a = [1,2,3,4,5,6]
print(a[-3::-1])