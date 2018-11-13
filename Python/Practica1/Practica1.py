'''
Created on 13 nov. 2018

@author: Iván
'''

#Lista de los numeros (Operandos)
# Pila de operadores, si es el primero lo guardo, si no, pues miro la prioridad del que hay y el que viene
#Si tienen misma prioridad o menos, desapilo
# Distinta prioridad dentro de la pila y fuera
# Si tengo un cierre de parentesis, tengo que desapilar
#Funcion isDigits() y Split()

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

def primero(cola):
    return cola[-1]

def preordenIn (operador):
    if operador == "(" :
        return 0
    elif operador == "+"  or operador == "-" :
        return 1
    elif operador == "*" or operador == "/" :
        return 2
    elif operador == "^" :
        return 3
    
def preordenOut (operador):
    if operador == "(" :
        return 5
    elif operador == "+"  or operador == "-" :
        return 1
    elif operador == "*" or operador == "/" :
        return 2
    elif operador == "^" :
        return 4
    
def postFija (lista):
    pf = []
    pila = []  
    for elemento in lista:
        if elemento.isdigit() :
            pf.append(elemento)
        else:
            if len(pila) == 0 : # Pila Vacia
                apilar(pila, elemento)
            elif elemento == ")": #Caso peculiar, si llego al cierre resuelvo. Recorro todo desapilando hasta (
                while cima(pila) != "(":
                    pf.append(desapilar(pila)) # Desapilo guardando en postfija pf 
                desapilar(pila)
            elif preordenIn(cima(pila) ) < preordenOut(elemento) : # Si es de mayor prioridad apilo sin más
                apilar(pila, elemento)
            else: 
                while len(pila) != 0 and preordenIn(cima(pila) ) >= preordenOut(elemento) : # Si es menor prioridad o igual
                    pf.append(desapilar(pila))
                apilar(pila, elemento)
            
    while len(pila) != 0 :
        pf.append(desapilar(pila))
    return pf
            
    
def solve (expresion):
    l = expresion.split()
    print(l)
    pf = postFija(l)
    print(pf)
    return print(resultado(pf))
 
def calc (a,b,o):
    if  o == "+" :
        return str(int(a) + int(b))
    elif o == "-":
        return str(int(a) - int(b))   
    elif o == "*":
        return str(int(a) * int(b)) 
    elif o == "/":
        return str(int(a) // int(b)) 
    elif o == "^":
        return str(int(a) ** int(b))   
    
def resultado (listaPF):
    pila = []
    for e in listaPF :
        if e.isdigit() :
            apilar(pila, e)
        else : 
            b = desapilar(pila)
            a = desapilar(pila)
            apilar(pila, calc(a,b,e))
    return cima(pila)
    
expresion = ' 4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
solve(expresion)