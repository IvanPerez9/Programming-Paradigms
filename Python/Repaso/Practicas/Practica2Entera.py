'''
Created on 8 jan. 2018

@author: IvánPerez9
'''

import collections
import numpy as np

"""
Rastrerizacion:

Tipo de dato imagen, de 10x10 , una matriz de numeros con numpy 
"""

####


Punto = collections.namedtuple("Punto" ,["x" , "y"])
Recta = collections.namedtuple("Recta" , ["v0" , "v1" ])
Triangulo = collections.namedtuple("Triangulo" , ["p0" , "p1" , "p2"])
Rectangulo = collections.namedtuple("Rectangulo" ,["p0" , "p1"] )
Cuadrilatero = collections.namedtuple("Cuadrilatero" , ["t1" , "t2"]) #Dos rectangulos

def construirCuadrilatero (p1,p2,p3,p4):
    t = Triangulo(p1,p2,p3)
    t2 = Triangulo(p1,p4,p3)
    c = Cuadrilatero(t,t2)
    return c

def limpiarImg (screen):
    return screen.zeros((10,10))

def modificarPantalla (img, fila, columna, valor):
    img[columna][fila] = valor

def imprimirPantalla (screen):
    print(screen)

def estaDentro (rect , point):
    return rect.p0.x <= point.x <= rect.p1.x and rect.p0.y <= point.y <= rect.p1.y

def borde (recta, punto):
    return  (punto.x - recta.v0.x) * (recta.v1.y - recta.v0.y) - (punto.y - recta.v0.y) * (recta.v1.x - recta.v0.x)

def estaTriangulo (triangulo, punto):
    r = Recta(triangulo.p0 , triangulo.p1)
    s = Recta(triangulo.p1 , triangulo.p2)
    t = Recta(triangulo.p2 , triangulo.p0)
    return (borde(r,punto) <= 0) and (borde(s,punto)<=0) and (borde(t,punto) <= 0)

def rasterize (screen , rect , value):
    file,column = screen.shape
    for i in range(file):
        for j in range(column):
            p = Punto(j,i)
            if estaDentro(rect, p ):
                modificarPantalla(screen, i,j,value)

def rasterizeT (screen , triangle , value):
    file,column = screen.shape
    for i in range(file):
        for j in range(column):
            p = Punto(j,i)
            if estaTriangulo(triangle, p):
                modificarPantalla(screen, i,j,value)

def rasterizarCuadrilatero (screen, cuadrilatero, value):
    fila, columna = screen.shape
    for i in range(fila):
        for j in range(columna):
            p = Punto(j,i)
            if (estaTriangulo(cuadrilatero.t1 , p) or estaTriangulo(cuadrilatero.t2 , p) ):
                modificarPantalla(screen, i, j, value)


if __name__ == '__main__':
    screen = np.zeros((10,10))
    imprimirPantalla(screen)

    p = Punto(3, 4)
    q = Punto(7, 8)
    p0 = Punto(7, 1)
    p1 = Punto(5, 9)
    p2 = Punto(1, 3)
    tri = Triangulo(p0,p1,p2)
    r = Rectangulo(p, q)

    #rasterize(screen, r , 4)
    rasterizeT(screen,tri,4)
    imprimirPantalla(screen)