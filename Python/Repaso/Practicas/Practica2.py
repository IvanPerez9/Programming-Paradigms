'''
Created on 29 dec. 2018

@author: IvanPerez9
'''
import numpy as np
import collections

"""
Rastrerizacion:

Tipo de dato imagen, de 10x10 , una matriz de numeros con numpy 
"""

####

"""
La imagen será representada como una matriz con valores numéricos (que representan color). Se
utilizará el módulo numpy para crear la imagen junto a las siguientes funciones:
 Definir una función que limpie la imagen y ponga todos sus pixeles a cero.
 Definir una función que imprime por pantalla la imagen
 Definir una función que permite modificar el valor de un pixel de la imagen.
"""

"""
El rasterizador más sencillo de construir es el que permite rasterizar un rectángulo alineado a los
ejes (AABB – axis aligned bounding box). Se pide:

 Definir el tipo de dato que representa un rectángulo.
Puede ser conveniente definir otros tipos de datos como puntos y/o vértices.
Un rectángulo alineado con los ejes está definido por 2 puntos, su esquina superior izquierda y
su esquina inferior derecha.
 Crear un método que rasterice un rectángulo alineado.
Recibirá una imagen, el rectángulo y el color (un entero).
Por cada pixel de la imagen (elemento de la matriz) comprobará si cae dentro del área del
rectángulo, de ser así cambiará su valor por el color recibido
"""

def limpiarPantalla (screen):
    return screen.fill(0)

def imprimirImagen (img, fila, columna, valor):
    img[fila][columna] = valor

#Definir tipos de datos para un rectangulo

Point = collections.namedtuple("Punto" , ["x" , "y"])
Rectangle = collections.namedtuple("Rectangle" , ["p1" , "p2"])

#Metodo que Raserice el rectangulo
#Primero un "comprobar si esta dentro o no"

def isIn (rect, point):
    return rect.p1.x <= point.x <= rect.p2.x and rect.p1.y <= point.y <= rect.p2.y

def rasterize (screen, rectangle, value):
    file, column = screen.shape
    for i in range(file):
        for e in range(column):
            point = Point(e,i)
            if isIn(rectangle,point):
                screen[i][e] = value

#Principal
if __name__ == '__main__':

    screen = np.zeros((10,10))
    print(screen)

    p = Point(3,4)
    q = Point(7,8)
    r = Rectangle(p,q)

    print(r)
    rasterize(screen,r,4)
    print(screen)