import numpy as np
import collections

def limpiarImagen (screen):
    return screen.fill(0)

def pintarPantalla (screen, fila, columna, color):
    screen[columna][fila] = color

def imprimirPanatlla (screen):
    print(screen)

Punto = collections.namedtuple("Punto" , ["x" , "y"])
Rectangulo = collections.namedtuple("Rectangulo" , ["p1" , "p2"])

def isIn (punto, rectangulo):
    return (rectangulo.p1.x <= punto.x <= rectangulo.p2.x) and (rectangulo.p1.y <= punto.y <= rectangulo.p2.y)


def rasterizadorRectangulo (screen, rectangulo, color) :
    fila, columna = screen.shape #Tamaño matriz
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if (isIn(p,rectangulo)):
                pintarPantalla(screen,i,e,color)

# Rasterizador triangulo

Recta = collections.namedtuple("Recta" , ["p1" , "p2"])
Triangulo = collections.namedtuple("Triangulo" , ["p1" , "p2" , "p3"])

def edge (recta, punto):
	return (punto.x - recta.p1.x) * (recta.p2.y - recta.p1.y) - (punto.y - recta.p1.y) * (recta.p2.x - recta.p1.x)

def isInTriangle (punto , triangle):
    s = Recta(triangle.p1 , triangle.p2)
    t = Recta(triangle.p2 , triangle.p3)
    r = Recta(triangle.p3 , triangle.p1)
    return (edge(s , punto) >= 0) and (edge(t, punto) >= 0) and (edge(r, punto) >= 0)

def rasterizarTriangulo (screen, triangulo, color):
    fila, columna = screen.shape
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if isInTriangle(p, triangulo):
                pintarPantalla(screen, i, e , color)

# Rasterizador poligonos -> Cuadrilateros

Cuadrilatero = collections.namedtuple("Cuadrilatero" , ["t1" , "t2"])

def rasterizarCuadrilatero (screen, poligono, color):
    fila, columna = screen.shape
    for i in range(fila):
        for e in range(columna):
            p = Punto(e,i)
            if (isInTriangle(p , poligono.t1)) or isInTriangle(p , poligono.t2) :
                pintarPantalla(screen, i , e , color)

if __name__ == '__main__':
    screen = np.zeros((10, 10))
    imprimirPanatlla(screen)

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

    c = Cuadrilatero(t1, t2)

    rasterizadorRectangulo(screen , r , 2)
    #rasterizarTriangulo(screen , tri , 3)
    #rasterizarCuadrilatero(screen, c, 4)

    imprimirPanatlla(screen)



if __name__ == '__main__':
    screen = np.zeros((10,10))
    imprimirPanatlla(screen)


