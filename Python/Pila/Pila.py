'''
Created on 13 nov. 2018

@author: Iván
'''
#Implemento una lista con un append, por como se hace el pop
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()

def cima(pila):
    return pila[-1]

def encolar(cola, elemento):
    cola.insert(0,elemento)
    
def desencolar (cola):
    return cola.pop()
    #Si lo uso el append en vez de inser , no usar el pop

def primero(cola):
    return cola[-1] #esta implementacion obliga a que el primeo de mi cola es el ultimo de mi lista

def balanceados(cadena):
    pila = []
    for i in cadena:
        if i == "(" :
            apilar(pila, i)
        elif i == ")" :
            if len(pila)==0 :
                print("Cadena desbalanceada")
                break
                desapilar(pila)
    if len(pila) == 0:
        print("Cadena balanceada")
    else:
        print("Cadena desbalanceada")
           
inputCola = input("Introduzca la cadena para parentesis balanceados: ")
balanceados(inputCola)


