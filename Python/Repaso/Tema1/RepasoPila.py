'''
Created on 17 nov. 2018

@author: Ivan
'''

"""
DIAPOS 41/42 Repaso de los metodo de la pila y ejercicios
"""

#APILAR

def apilar (pila, elem):
    pila.append(elem)

#DESAPILAR

def desapilar (pila):
    return pila.pop()

#CIMA devuelve el ultimo elemento, como en una lista

def cima (pila):
    return pila[-1] 

#ENCOLAR lo mismo pero con colas, una lista que simule una cola

def encolar (cola, elem):
    return cola.insert(0,elem)

cola = [1,2,3]
print(cola)
apilar([1,2,3] , 4)
print(cola)

def desencolar (cola):
    return cola.pop()

def primero(cola):
    return cola[-1]

#Parentesis Balanceados 

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
    
    