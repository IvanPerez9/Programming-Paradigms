'''
Created on 21 dec 2018

@author: Iván
'''

#Trabajar con pilas y colas

def apilar (pila,e):
    pila.append(e)

def desapilar (pila):
    return pila.pop()

def cima (pila):
    return pila[-1]

def encolar (cola,e):
    cola.insert(0,e)

def desencolar (cola):
    return cola.pop()

def primero (cola):
    return cola[-1]

def preordenIn (operador):
    if operador == "(":
        return 0
    elif operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador == "/":
        return 2
    elif operador == "^":
        return 3

def preordenOut (operador):
    if operador == "(":
        return 5
    elif operador== "+" or operador=="-":
        return 1
    elif operador == "*" or operador=="/":
        return 2
    elif operador == "^":
        return 4

def postFija (lista):
    postFija = []
    auxOperadores = []
    for e in lista:
        if e.isdigit() :
            apilar(postFija,e)
        else:
            if len(auxOperadores) == 0:
                apilar(auxOperadores,e)
            elif preordenIn(e) > preordenOut(cima(auxOperadores)) :
                apilar(auxOperadores,e)
            elif e == ")" :
                while cima(desapilar(auxOperadores)) != "(" :
                    apilar(postFija, desapilar(auxOperadores))
                desapilar(auxOperadores)
            else:
                apilar(postFija,desapilar(auxOperadores))



lista1 = [1,2,3,4,5,6]

lista2 = lista1[:]

print(lista2)

"""
Lista : Coleccion Heterogenea , ordenado y mutable
Set : Coleccion desordenada, mutable de objetos hasheables
Frozetset : Coleccion inmutable, por lo que es hasheable
Diccionarios: Coleccion clave valor, la clave a de ser hasheable
"""

