
"""
Estafa cara o cruz
"""
import random

# Funcion que simule el lanzamiento de una moneda

def lanzamiento ():
    moneda = random.randint (0 ,1)
    if moneda == 1 :
        return "H"
    else:
        return "T"

# Crear funcion que mientras no se dé una secuencia de cara o cruz, siga lanzando

def sequence (seq):
    lanzar = lanzamiento()
    while seq not in lanzar:
        lanzar += lanzamiento()
    return lanzamiento

print(sequence("HTHT"))

# Modificar para recibir 2 secuencias, hasta que una se cumpla y devolver la ganadora junto con el numero de lanzamientos

def seqGanadora (seq1 ,seq2):
    lanzar = lanzamiento();
    contador = 1;
    while seq1 not in lanzar and seq2 not in lanzar:
        lanzar += lanzamiento()
        contador += 1
    if seq1 in lanzar:
        print ("Secuencia ganadora " + seq1 + " con " + contador + " tiradas")
    else:
        print ("Secuencia ganadora " + seq2 + " con " + contador + " tiradas")

seqGanadora ("THT" , "THH")

# Modificar para que devuelva el que gana 100 partidas

def win (seq1, seq2):
    lanzar = lanzamiento();
    while seq1 not in lanzar and seq2 not in lanzar:
        lanzar += lanzamiento()
    if lanzar in seq1:
        return seq1
    else:
        return seq2


def ganar100 (seq1 ,seq2):
    win1 = 0
    win2 = 0
    for i in range(100):
        if (win(seq1 ,seq2) == seq1):
            win1 += 1
        else:
            win2 += 1

    if win1 > win2 :
        print ("Gana la secuencia 1")
    else:
        print ("Gana la secuencia 2")
