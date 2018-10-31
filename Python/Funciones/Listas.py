'''
Created on 31 oct. 2018

@author: Ivan
'''

#Dada una lista imprimir los elementos que esten en posicion par

lista = [1,2,3,4,5,6]

def pares (lista):
    for i in range(0,len(lista),2):
        print(lista[i])
    
pares(list(range(10)))
pares(lista)