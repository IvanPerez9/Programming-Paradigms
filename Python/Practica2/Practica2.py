'''
Created on 4 dec. 2018

@author: Iván
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

def clearscreen (screen): # Borrar la pantalla
    return screen.fill(0)

def setPixel (imagen, f,c,v): # Fila, columna, valor
    imagen[f][c] = v

Point = collections.namedtuple("Point" , [ "x" , "y"])
Rectangle = collections.namedtuple("Rectangle" , [ "min" , "max"])

def estaDentro (rect , x,y):
    return rect.min.x <= x <= rect.max.x and rect.min.y <= y <= rect.max.y

def rasterizar (screen, rect, value): #Valor es el color
    fila, columna = screen.shape #Shape funcion de numpy
    for i in range(fila):
        for j in range(columna):
            if estaDentro(rect, j, i):
                screen[i][j] = value # Pintarlo

if __name__ == "__main__":
    screen = np.zeros((10,10))
    print(screen)
    p = Point (3,4)
    q = Point (7,8)
    #print(p)
    #print(p[0])
    #print(p.x)
    r = Rectangle (p, q)
    print(r)
    print(r.min.x)
    rasterizar(screen, r , 2)
    print(screen)
    """ PRUEBAS
    setPixel(screen, 2,3,4) # Fila 2, columna 3 poner un 4
    print(screen)
    screen[0] = 2
    print(screen)
    clearscreen(screen)
    print(screen)
    """

"""
Básicamente, lo que haces usando if __name__ == “__main__”: es ver si el módulo ha sido importado o no. 
Si no se ha importado (se ha ejecutado como programa principal) ejecuta el código dentro del condicional.

Una de las razones para hacerlo es que, a veces, se escribe un módulo (un archivo .py) que se puede ejecutar 
directamente, pero que alternativamente, también se puede importar y reutilizar sus funciones, clases, métodos,
etc en otro módulo. Con esto conseguimos que la ejecución sea diferente al ejecutar el módulo directamente 
que al importarlo desde otro programa.
"""

######