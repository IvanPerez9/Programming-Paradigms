"""
Tener una pila de operadores -> Operaciones de pila
Funciones de prioridad dentro de la pila y fuera

Si tiene misma prioridad o menos, desapilo -> Acumulando en postfija
Si tiene un cierre de parentesis desapilo
Si la prioridad a entrar es mayor que la del elemento cima se apila

Tener en cuenta isdigit() y split()
"""

def apilar (pila, elemento):
    pila.append(elemento)

def desapilar (pila):
    return pila.pop()

def cima (pila):
    return pila[-1]

def encolar (cola, elemento):
    cola.insert(0, elemento)

def desencolar (cola):
    return cola.pop()

def primero(cola):
    return cola[-1]

def preOrdenIn (elemento):
    if elemento == "(" :
        return int(0)
    elif elemento == "+" or elemento == "-" :
        return int(1)
    elif elemento == "*" or elemento == "/":
        return int(2)
    elif elemento == "^" :
        return int(3)

def preOrdenOut (elemento):
    if elemento == "(" :
        return int(5)
    elif elemento == "+" or elemento == "-":
        return int(1)
    elif elemento == "*" or elemento == "/" :
        return int(2)
    elif elemento == "^" :
        return int(4)

def convertirEnPostFija (lista):
    pf = []
    pila = []
    for e in lista:
        if e.isdigit() :
            pf.append(e)
        else:
            type(e)
            if len(pila) == 0 : #Es el primer operador
                apilar(pila, e)
            elif e == ")" : #Desapilar hasta encontrar un (
                while cima(pila) != "(" :
                    pf.append(desapilar(pila))
                desapilar(pila)
            elif preOrdenIn(cima(pila)) < (preOrdenOut(e)):
                apilar(pila,e)
            else:
                while len(pila) != 0 and preOrdenIn(cima(pila)) >= preOrdenOut(e) :
                    pf.append(desapilar(pila))
                apilar(pila,e)
    while len(pila) != 0:
        pf.append(desapilar(pila))

    return pf

"""
Ir leyendo la expresion postfija de izqu a derecha

- Si es un operando lo apilamos en la pila
- Si es un operador, extraemos 2 operandos, aplicamos el operador, y el resultado lo apilamos
- Si el orden importa, el primero a la derecha y el segundo a la izq de la operacion

Nos quedará una expresion de un solo numero
"""

def calcular (a,b, operador) :
    if operador == "+" :
        return str (int(a) + int(b))
    elif operador == "-" :
        return str (int(a) - int(b))
    elif operador == "*" :
        return str (int(a) * int(b))
    elif operador == "/" :
        return str (int(a) // int(b))
    elif operador == "^" :
        return str (int(a) ** int(b))

def resolver (pf):
    pilaAux = []
    for e in pf:
        if e.isdigit():
            apilar(pilaAux,e)
        else:
            b = desapilar(pilaAux)
            a = desapilar(pilaAux)
            apilar(pilaAux, calcular(a,b,e))
    return cima(pilaAux)

if __name__ == '__main__':
    expresion = ' 4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
    lista = expresion.split()
    print(lista)
    pf = convertirEnPostFija(lista)
    print(pf)
    print(resolver(pf))