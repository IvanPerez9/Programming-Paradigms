'''
Created on 5 dec. 2018

@author: Iván
'''

import collections
import numpy as np


"""
Rasterizando triángulos
Para rasterizar un triangulo es necesario tener una función que determine cuando un pixel está
dentro del área definida por 3 puntos.
"""

# Colecciones mutables, lista, diccionarios, conjuntos
# No mutable un frozen set

# Formaula de borde: Si estan en la linea en 0, sino da < o > que 0, para saber a que lado del
# Poligono está. Para ello necesitamso una estructura recta
# El rextangulo está sujeto a 3 puntos

# El orden de los vertices importa, para saber si a derecha o a izq está el negativo o positivo.
# Asegurar que vienen segun las agujar del reloj

"""
Esta función E cumple que, dada una recta (compuesta por 2 vértices) y un punto, devuelve:
o E(recta, punto) > 0 si el punto está a la derecha de la recta.
o E(recta, punto) = 0 si el punto está en la recta.
o E(recta, punto) < 0 si el punto está a la izquierda de la recta
"""

Point = collections.namedtuple("Point" , [ "x" , "y"])
Recta = collections.namedtuple("Recta" , [ "v0" , "v1"])
Triangle = collections.namedtuple("Triangle" , ["p1" , "p2" , "p3"]) #Tres puntos, pero Python no tiene tipos

def borde (recta, punto):
    return (punto.x - recta.v0.x) * (recta.v1.y - recta.v0.y) - (punto.y - recta.v0.y) * (recta.v1.x - recta.v0.x)

def inTriangle (triangle, point):
    r = Recta(triangle.p1, triangle.p2)
    s = Recta(triangle.p2, triangle.p3)
    t = Recta(triangle.p3, triangle.p1)
    return (borde(r, point) <=0) and (borde(s, point) <= 0 )and (borde(t, point) <= 0)

def rasterizar (screen, triangulo, value): #Valor es el color
    fila, columna = screen.shape #Shape funcion de numpy
    for i in range(fila):
        for j in range(columna):
            if inTriangle(triangulo, Point(j,i)):
                screen[i][j] = value # Pintarlo


if __name__ == "__main__":
    screen = np.zeros((10,10))
    print(screen)
    p = Point(7, 1)
    p1 = Point(5,9)
    p2 = Point (1,3)
    r = Recta (p, p2)
    t = Triangle (p, p1 , p2)
    print(borde(r, p1))
    rasterizar(screen,t, 3 )
    print(screen)


# Coleccion de triangulos para lo siguiente de los poligonos