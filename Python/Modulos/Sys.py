'''
Created on 4 dec. 2018

@author: Iván
'''

"""
Para hacer modulos mirar el modulo sys. Es solo teorico, no vamos a hacer ejercicios sobre esto.
Mirar bien la teoria, sobretodo lo de los nombres, para evitar que cargen modulos
Diapo 20 en T2 
"""

"""
Usar un namedTuple para tener estructuras tipo C 

deque: Insercion como eliminacion de la lista por cabecera y final es eficiente
Sin insert, y pop. Es ineficiente el insert, porque desplaza toda la lista para insertar.
El pop y append es eficiente.
SI NECESITAMOS UNA COLA MEJOR DEQUE

OrederedDict: Diccionario ordenado, no es el orden de los elementos, si no está ordenado por el orden de insercion.
Recorre por el orden de insercion, de forma eficiente.

Counter: Lleva la cuenta de los objetos, de la clave. Cuando numeros de usa un elemento.
Diccinario especifico para contrar claves.

"""


###############


"""
Una queja es que no hay array, que se usa una lista, pero son listas de punteros.
Python define el modulo array, con tamaño y tipo en su creacion -> no se usa casi

Aparecio un modulo, numpy , que era la primera implementacion de array compatibles con funciones de C

import numpy as np ---- SIEMPRE !!! 

Permite iterar con las listas de Python, np.array([1,2,3]) es más eficiente que la lista
Aqui se crea a traves de una lista

"""