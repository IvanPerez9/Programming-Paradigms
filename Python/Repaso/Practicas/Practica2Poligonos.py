'''
Created on 30 dec. 2018

@author: IvánPerez9
'''

import collections
import numpy as np

"""
Para rasterizar polígonos con N vértices se hace uso del rasterizador de triángulos. Para ello,
hay que definir los polígonos como una colección de triángulos.
El caso más sencillo es un polígono de 4 vértices (cuadrilátero). Para rasterizar un cuadrilátero
necesitamos 2 triángulos. Si v0, v1, v2 y v3 son los vértices de un cuadrilátero, sus triángulos
serán (v0, v1, v2) y (v2, v3, v0). Se pide:
 Definir un cuadrilátero como 2 triángulos.
 Crear una función que dados los 4 vértices de un cuadrilátero construya la estructura
anteriormente definida.
 Crear un método que, dada una imagen, un cuadrilátero y un color, rasterize dicho
cuadrilátero.

Vértices: v0, v1, v2, v3
Índices: 0, 1, 2, 2, 3, 1
Se pide:
 Definir la nueva estructura de un polígono.
Será necesario guardar el número de lados del polígono.
 Crear un método que pueda rasterizar esta nueva estructura.
"""

Punto = collections.namedtuple("Point" , [ "x" , "y"])
Recta = collections.namedtuple("Line" , [ "v0" , "v1"])
Triangulo = collections.namedtuple("Triangle" , ["p1" , "p2" , "p3"])
Cuadrilatero = collections.namedtuple("Quadrilateral" , ["t1" , "t2"])

def construirCuadrilatero (p1,p2,p3,p4):
    t = Triangulo(p1,p2,p3)
    t2 = Triangulo(p1,p4,p3)
    c = Cuadrilatero(t,t2)
    return c

#Hacer uso de lo del triangulo

def borde (recta, punto):
    return (punto.x - recta.v0.x) * (recta.v1.y - recta.v0.y) - (punto.y - recta.v0.y) * (recta.v1.x - recta.v0.x)

def inTriangle (triangle, punto):
    r = Recta(triangle.p1, triangle.p2)
    s = Recta(triangle.p2, triangle.p3)
    t = Recta(triangle.p3, triangle.p1)
    return (borde(r, punto) <= 0) and (borde(s, punto) <= 0) and (borde(t, punto) <= 0)

def rasterizarCuadrilatero (screen, cuadrilatero, value):
    fila, columna = screen.shape
    for i in range(fila):
        for j in range(columna):
            p = Punto(j,i)
            if (inTriangle(cuadrilatero.t1 , p) or inTriangle(cuadrilatero.t2 , p) ):
                screen[j][i] = value

if __name__ == '__main__':
    screen = np.zeros((10,10))
    print(screen)
    print()

    p = Punto(2, 4)
    q = Punto(5, 3)
    s = Punto(5, 6)
    l = Punto(2, 6)

    r = Recta(p, q)
    r1 = Recta(q, s)
    r2 = Recta(s, p)
    r11 = Recta(s, l)
    r22 = Recta(l, p)
    r33 = Recta(p, s)

    t1 = Triangulo(p, q, s)
    t2 = Triangulo(s, l, q)

    c = Cuadrilatero(t1,t2)

    rasterizarCuadrilatero(screen, c , 4)

    print(screen)