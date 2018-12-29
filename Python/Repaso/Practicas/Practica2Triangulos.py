'''
Created on 29 dec. 2018

@author: IvánPerez9
'''

import collections
import numpy as np

"""
Rasterizando triángulos
Para rasterizar un triangulo es necesario tener una función que determine cuando un pixel está
dentro del área definida por 3 puntos.
 Definir las estructuras necesarias para rasterizar un triangulo.
Un triangulo está formado por 3 vértices.
 Crear la función borde que recibe una recta y un punto.
"""

Point = collections.namedtuple("Punto" , ["x" , "y"])
Line = collections.namedtuple("Recta" , ["v0" , "v1"])
Triangle = collections.namedtuple("Triangulo" , ["r1" , "r2" , "r3"])

def edge (punto , recta):
    return (punto.x - recta.v0.x) * (recta.v1.y - recta.v0.y) - (punto.y - recta.v0.y) * (recta.v1.x - recta.v0.x)

"""
Esta función E cumple que, dada una recta (compuesta por 2 vértices) y un punto, devuelve:
o E(recta, punto) > 0 si el punto está a la derecha de la recta.
o E(recta, punto) = 0 si el punto está en la recta.
o E(recta, punto) < 0 si el punto está a la izquierda de la recta.
"""

"""
 Crear una función que devuelve si un punto está dentro de un triangulo.
Un punto está dentro de un triangulo si, al evaluar la función borde sobre los vértices
recorridos en sentido horario, el resultado de las 3 rectas es igual o mayor que 0.
 Crear un método que rasterize un triangulo.
Recibirá una imagen, un triangulo y el color (un entero).
Por cada pixel de la imagen (elemento de la matriz) comprobará si cae dentro del área del
rectángulo, de ser así cambiará su valor por el color recibido.
"""

def inTriangle (point , triangle):
    r = Line(triangle.r1 , triangle.r2)
    s = Line(triangle.r2, triangle.r3)
    t = Line(triangle.r3, triangle.r1)
    return (edge(point,r)<= 0) and (edge(point,s) <= 0) and (edge(point,t) <= 0)

def rasterizeTriangle (screen, triangle, value):
    file,column = screen.shape
    for i in range(file):
        for j in range(column):
            if inTriangle(Point(j,i) , triangle):
                screen[j][i] = value

if __name__ == '__main__':

    screen = np.zeros((10,10))
    print(screen)
    p = Point(7, 1)
    p1 = Point(5,9)
    p2 = Point (1,3)
    r = Line (p, p2)
    t = Triangle (p, p1 , p2)
    print(edge(p1,r))
    rasterizeTriangle(screen,t, 3 )
    print(screen)
