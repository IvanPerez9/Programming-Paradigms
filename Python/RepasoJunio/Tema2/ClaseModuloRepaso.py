import random

# Funcion que simule el lanzamiento de una moneda
def lanzamiento():
    n = random.randint(0, 1)
    if round(n) == 1:
        return("T")
    else:
        return("H")

#Mientras no se de una secuencia siga lanzando
def sequence (seq):
    aux = lanzamiento()
    while seq not in aux:
        aux += lanzamiento()
    return aux

#print(sequence("HTT"))

#Dos secuancias y lance la moneda hasta que una de las dos se cumple. Devolver ganadora y numero de lanzamientos
def ganador (seq1, seq2):
    contador = 0;
    lanzar = lanzamiento()
    while seq1 not in lanzar and seq2 not in lanzar:
        contador += 1
        lanzar += lanzamiento()
    if seq1 in lanzar:
        print("Secuencia " + seq1 + " con " + str(contador) + " lanzamientos")
    elif seq2 in lanzar:
        print("Secuencia " + seq2 + " con " + str(contador) + " lanzamientos")

def ganador2 (seq1, seq2):
    contador = 0;
    lanzar = lanzamiento()
    while seq1 not in lanzar and seq2 not in lanzar:
        contador += 1
        lanzar += lanzamiento()
    if seq1 in lanzar:
        return seq1
    elif seq2 in lanzar:
        return seq2

#Lo mismo, pero hasta que no lleguen a 100 ganadas una de las dos no para
def ganador100 (seq1 , seq2):
    contador1 = 0
    contador2 = 0
    while contador1 != 100 and contador2 != 100:
        n = ganador2(seq1,seq2)
        if (n == seq1):
            contador1 += 1
        else:
            contador2 += 1

    if contador1 == 100:
        print("Ha ganado: " + seq1 + " con diferencia de: " + str(contador1 - contador2))
    else:
        print("Ha ganado: " + seq2 +  " con diferencia de: " + str(contador2 - contador1))

ganador100("THH" , "HTT")