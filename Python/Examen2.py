"""
Uno de los problemas de las primeras maquinas arkade era como mostrar una imagen de baja resolución
en pantallas grandes. Una de las tecnicas desarrolladas para resolver esto se llama scanline que
consiste en intercalar filas de pixeles negros (ceros) entre pixeles con la información de color,
con lo que se conseguia duplicar el número de lineas a mostrar.

Se pide implementar un script que dada una matriz de numpy, genere, aplicando el scanline,
otra matriz con el doble de alto.

Ej:

                    [[1 2 3 4]
[[1 2 3 4]           [0 0 0 0]
 [5 6 7 8]      ->   [5 6 7 8]
 [9 0 1 2]]          [0 0 0 0]
                     [9 0 1 2]]

El script empezara con la siguiente creación de variables:

a = np.random.randint(255, size=(240, 640))
b = np.zeros((480, 640))
Se pide, escribir las instruciones necesarias para que "b" tenga los valores esperados
(el contenido de "a" con filas de ceros intercalados).
Como es un script, será necesario proteger las instrucciones para que no sean ejecutadas en
caso de que erroneamente un usuario de nuestro script lo importe como un módulo. (1 punto)
"""

import numpy as np

arr = np.arange(12).reshape(3,4)
print(arr)

for i in range(4):
    if (4 % (i+1) != 0):
        a = arr.insert(arr , [i-1] , [[0]] , axis = 0 ) # Axis = 0 es por fila , con 1 es por columna
        a = arr.insert(a , [i+1] , [[0]] , axis = 0) # Repetir para la ultima fila o primera

print(a)

