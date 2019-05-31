"""
La imagen será representada como una matriz con valores numéricos (que representan color). Se
utilizará el módulo numpy para crear la imagen junto a las siguientes funciones:
- Definir una función que limpie la imagen y ponga todos sus pixeles a cero.
- Definir una función que imprime por pantalla la imagen
- Definir una función que permite modificar el valor de un pixel de la imagen.
"""

import numpy as np
import collections

"""
El rasterizador más sencillo de construir es el que permite rasterizar un rectángulo alineado a los
ejes (AABB – axis aligned bounding box). Se pide:

- Definir el tipo de dato que representa un rectángulo.
Puede ser conveniente definir otros tipos de datos como puntos y/o vértices.
Un rectángulo alineado con los ejes está definido por 2 puntos, su esquina superior izquierda y
su esquina inferior derecha.
- Crear un método que rasterice un rectángulo alineado.
Recibirá una imagen, el rectángulo y el color (un entero).
Por cada pixel de la imagen (elemento de la matriz) comprobará si cae dentro del área del
rectángulo, de ser así cambiará su valor por el color recibido
"""

Punto = collections.namedtuple("Punto" , ["x" , "y"])
Rectangulo = collections.namedtuple("Rectangulo" , ["p1" , "p2"])

# Metodos para la matriz o imagen

def limpiarPantalla (screen):
    return screen.fill(0)

def pintarPantalla (img , fila, columna, color):
    img[columna][fila] = color

def imprimirPantalla (screen):
    print(screen)

# RASTERIZADOR PARA UN RECTANGULO

def isIn (punto, rectangulo):
    return (rectangulo.p1.x <= punto.x <= rectangulo.p2.x) and (rectangulo.p1.y <= punto.y <= rectangulo.p2.y)

def rasterizeRectangulo (screen , rectangulo, color):
    fila, columna = screen.shape #El tamaño de la matriz
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if isIn(p , rectangulo):
                pintarPantalla(screen , i , e, color)

# RASTERIZADOR CON UN TRIANGULO

Recta = collections.namedtuple("Recta" , ["p1" , "p2"])
Triangulo = collections.namedtuple("Triangulo" , ["p1" , "p2" , "p3"])

# Si es punto esta a la derecha > 0 , a la izq < 0 y en la recta = 0
def edge (recta, punto):
	return (punto.x - recta.p1.x) * (recta.p2.y - recta.p1.y) - (punto.y - recta.p1.y) * (recta.p2.x - recta.p1.x)

def isInTriangulo (punto, triangulo):
    r = Recta(triangulo.p1 , triangulo.p2)
    s = Recta(triangulo.p2, triangulo.p3)
    t = Recta(triangulo.p3 , triangulo.p1)

    return (edge(r, punto) <= 0) and (edge(s , punto) <= 0) and (edge(t, punto) <= 0)

def rasterizeTriangulo (screen , triangulo , color):
    fila, columna = screen.shape # Tamaño matriz
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if isInTriangulo(p , triangulo):
                pintarPantalla(screen, i , e , color)

# RASTERIZADOR DE POLIGONOS

Poligono = collections.namedtuple("Poligono" , ["t1" , "t2"]) #Con dos triangulos

def rasterizeCuadrilatero (screen, poligono, color):
    fila, columna = screen.shape
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if (isInTriangulo(p , poligono.t1)) or isInTriangulo(p , poligono.t2) :
                pintarPantalla(screen, i , e , color)

if __name__ == '__main__':
    screen = np.zeros((10, 10))
    imprimirPantalla(screen)

    p = Punto(3, 4)
    q = Punto(7, 8)
    p0 = Punto(7, 1)
    p1 = Punto(5, 9)
    p2 = Punto(1, 3)
    r = Rectangulo(p, q)
    tri = Triangulo(p0, p1, p2)

    t = Punto(2, 4)
    q1 = Punto(5, 3)
    s = Punto(5, 6)
    l = Punto(2, 6)

    t1 = Triangulo(t, q1, s)
    t2 = Triangulo(s, l, q1)

    c = Poligono(t1, t2)

    #rasterizeRectangulo(screen , r , 2)
    #rasterizeTriangulo(screen , tri , 3)
    rasterizeCuadrilatero(screen, c, 4)

    imprimirPantalla(screen)