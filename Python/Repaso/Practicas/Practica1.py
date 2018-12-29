'''
Created on 21 dec 2018

@author: Iván
'''

#Trabajar con pilas y colas

def apilar (p,e):
    p.append(e)

def desapilar (p):
    return p.pop()

def cima (p):
    return p[-1]

def encolar (c,e): #Si no los inserto así no puedo usar pop luego
    c.insert(0,e)

def desencolar (c):
    return c.pop()

def primero (c):
    return c[-1]

# Creo las prioridades para los operadores, tanto dentro como fuera de la pila

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

"""
o Operando: se acumula en la expresión postfija que se lleve hasta el momento.
o Operador: se acumulará en la pila de operadores. Se pueden desapilar si pasan casos

     Si la prioridad del elemento a entrar es mayor que la del elemento cima, se apilará.
    
     En caso contrario (prioridad igual o menor), se desapilarán los elementos que
    forman la pila (y se irán acumulando en la expresión postfija) hasta encontrar un
    elemento con prioridad justamente inferior, provocando entonces el apilamiento
    de dicho operando.
    
     No obstante, hay un caso excepcional para los operadores. El operador “)”
    provocará el desapilamiento de los operadores que haya en la pila (y su
    acumulación en la expresión postfija) hasta encontrar el primer paréntesis abierto
    “(“. Ni este paréntesis abierto se incluirá en la expresión postfija ni el paréntesis
    cerrado se apilará en la pila
    
"""

#CONVERTIR LA EXPRESION INFIJA EN POSTFIJA

def postFija (lista):
    postFija = []
    pilaAux = []
    for elem in lista:
        if (elem.isdigit()) :
            postFija.append(elem)
        else:
            if len(pilaAux) == 0:
                apilar(pilaAux,elem) # Si es el primer elemento
            elif elem == ")" : #Caso excepcional, desapilar y acumular en postfija hasta (
                while (cima(pilaAux) != "(" ):
                    postFija.append(desapilar(pilaAux))
                desapilar(pilaAux)
            elif preordenOut(elem) > preordenIn(cima(pilaAux)) : #Si la prioridad es mayor apilar sin mas.
                apilar(pilaAux,elem)
            else:
                #Prioridad menor o igual
                # Desapilar hasta encontrar un elemento de prioridad inferior
                while len(pilaAux) != 0 and preordenIn(cima(pilaAux)) >= preordenOut(elem):
                    postFija.append(desapilar(pilaAux))
                apilar(pilaAux,elem)

    #Una vez terminada la expresion se desapilar todos los elementos restantes. Acumulados en postfija

    while len(pilaAux) != 0:
        postFija.append(desapilar(pilaAux))

    return postFija

"""
SEGUNDA FASE

leer postfija de izq a derch :

    o Si lo que nos encontramos es un operando: lo apilamos en la pila correspondiente.
    
    o Si lo que nos encontramos es un operador: extraemos los dos primeros operandos de la
    pila, aplicamos el operador con estos dos operandos y el resultado lo apilamos de nuevo en
    la pila. En el caso de ser una operación donde el orden importa, el primero de los
    operandos extraídos será el situado a la derecha del operador, mientras que el segundo
    extraído de la pila irá en primer lugar de la operación.
"""

# Resultado será el ultimo numero acumulado en la pila

def calcular (a,b,operandor):
    if operandor == "+":
        return str(int(a)+int(b)) #Son string, osea que operar y pasar otra vez a string
    elif operandor == "-":
        return str(int(a) - int(b))
    elif operandor == "*":
        return str(int(a) * int(b))
    elif operandor == "/":
        return str(int(a) // int(b))
    elif operandor == "^":
        return str(int(a) ** int(b))

def resultado (listaPostF):
    pilaResultado = []
    for elem in listaPostF:
        if elem.isdigit() :
            apilar(pilaResultado,elem)
        else:
            operador1 = desapilar(pilaResultado)
            operador2 = desapilar(pilaResultado)
            pilaResultado.append(calcular(operador2,operador1,elem))
            #apilar(pilaResultado,calcular(operador2,operador1,elem))

    return cima(pilaResultado)

def main (expresion):
    l = expresion.split()
    print("La expresion es: ")
    print(l)
    pf = postFija(l)
    return print(resultado(pf))

expresion = ' 4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
main(expresion)

#OJO LOS ISDIGIT ES EN MINUSCULAS