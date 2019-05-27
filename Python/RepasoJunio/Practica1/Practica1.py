
"""
Trabajar con pilas y colas
"""

def apilar (p,e):
    p.append(e)

def desapilar (p):
   return  p.pop()

def cima(p):
    return p[-1]

def encolar (c,e):
    c.insert(0,e)

def desencolar(c):
    return c.pop()

def primero(c):
    return c[-1]

"""
Prioridades de los objetos que encolo o apilo
"""

def dentroPila (op):
    if (op == '('):
        return 0
    elif ((op == '+') or (op == '-')):
        return 1
    elif ((op == '*') or (op == '/')):
        return 2
    elif (op == '^'):
        return 3
    else:
        print("El operador " + op +  " no existe")

def fueraPila (op):
    if (op == '('):
        return 5
    elif ((op == '+') or (op == '-')):
        return 1
    elif ((op == '*') or (op == '/')):
        return 2
    elif (op == '^'):
        return 4
    else:
        print("El operador " + op + " no existe")

"""
Operadores se acumular en una pila, en funcion de su prioridad desapilamos otros
- Si al entrar es mayor que la cima -> APILAR
- Si es menor o igual se desapila hasta encontrar un elemento menor prioridad
- Los ')' provacan desapilamiento si o si hasta un '('

Los operandos se acumular en la expresion postfija
"""

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
            elif fueraPila(elem) > dentroPila(cima(pilaAux)) : #Si la prioridad es mayor apilar sin mas.
                apilar(pilaAux,elem)
            else:
                #Prioridad menor o igual
                # Desapilar hasta encontrar un elemento de prioridad inferior
                while len(pilaAux) != 0 and dentroPila(cima(pilaAux)) >= fueraPila(elem):
                    postFija.append(desapilar(pilaAux))
                apilar(pilaAux,elem)

    #Una vez terminada la expresion se desapilar todos los elementos restantes. Acumulados en postfija

    while len(pilaAux) != 0:
        postFija.append(desapilar(pilaAux))

    return postFija


def calcular (a,b, operando):
    if (operando == "+"):
        return str(int(a) + int(b))
    elif operando == "-":
        return str(int(a) - int(b))
    elif operando == "*":
        return str(int(a) * int(b))
    elif operando == "/":
        return str(int(a) // int(b))
    elif operando == "^":
        return str(int(a) ** int(b))

def ret (listaPre):
    resultadoPF = []
    for e in listaPre:
        if e.isdigit() :
            apilar(resultadoPF, e)
        else:
            op1 = desapilar(resultadoPF)
            op2 = desapilar(resultadoPF)
            ret = calcular(op1,op2, e)
            apilar(resultadoPF,ret)

    return cima(resultadoPF)

def main (expresion):
    l = expresion.split()
    pf = postFija(l)
    result = ret(pf)
    print(result)

expresion = ' 4 - 5 ^ ( 5 - 2 ) + 9 * 7 - 24 / ( 7 - 2 ) '
main(expresion)