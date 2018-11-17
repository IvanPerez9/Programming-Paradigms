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


cola = [1,2,3]
print(cola)
encolar([1,2,3] ,4)
print(cola)
    
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

#MI BALANCEADO FUNCIONANDO ESTA EN LA HOJA DE REPASO

"""
def balanceados (cadena):
    
    p = []
    indice = 0
    while indice < len(cadena):
        simbolo = cadena[indice]
        if simbolo == "(":
            apilar(p, simbolo)
        elif simbolo == ")":
            if len(p) == 0:
                return print("No balanceado")
            else:
                desapilar(p)

        indice = indice + 1

    if len(p)==0:
        return print("Balanceado")
    else:
        return print("No balanceado")


cadenaPrueba = input("Introduce la cadena para probar ")
balanceados(cadenaPrueba)

"""


