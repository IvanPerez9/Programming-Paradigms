'''
Created on 11 nov. 2018

@author: Ivan
'''

def Ternas (listaT):
    
    """
    Recibir una lista de numeros y devuelva una tupla, con su elemento su cuadrado y su cubo
    Args:
        listaT = Lista de numeros que le entra
    Return:
        Cada numero en una terna, teniendo el propio numero, el cuadrado y el cubo del mismo
    """
    for i in range(1,len(listaT)+1):
        print(str( i) + ", " +str( i**2) + ", " + str(i*i*i) )

Ternas([1,2,3]);

# Print in one line ?????????????????????

def maxMin (listaM):
    """
    Devolver el maximo y el minimo de una lista de numeros
    Args:
        Le paso la lista de numeros
    Return:
        El maximo de la lista y el minimo de la lista
    """
    print("El maximo es: " + str(Maximo(listaM)))
    print("El minimo es: " + str(Minimo(listaM)))
    
def Maximo (lista):
    maximoLocal = 0
    for i in range (0,len(lista)):
        if lista[i] > maximoLocal :
            maximoLocal = lista[i]
        
    return maximoLocal  

def Minimo(lista):
    minimoLocal = Maximo(lista)
    for i in range (0,len(lista)):
        if lista[i] < minimoLocal :
            minimoLocal = lista[i]
        
    return minimoLocal 

maxMin([1,2,90,4,5,6,80]) 

def reverse(list):
    """
    Invertir una cadena en python
    Args: Entra la cadena, string
    Return: Devuelve la cadena invertirda
    """
    if len(list)==1:
        return list
    else:
        return list[-1]+reverse(list[:-1])

def invertir(var):
        return var[::-1]
    
cadena = input("Introduzca la cadena a invertir: ")
print(reverse(cadena))
print(invertir(cadena))  

def mayuscula (list):
    """
    Devolver la misma cadena solo que con la primera en mayuscula
    Args: Cadena de caracteres
    Return: Cadena de caracteres
    """      
    return list [0:1].upper() + list [1:]

cadenaMayus = input("Introduzca la cadena para mayusuclas: ")
print(mayuscula(cadenaMayus))

def area(base = 3, altura = 4):
     """Calcula el are de un rectángulo.
     Args:
     base (Number): base del rectángulo (3).
     altura (Number): altura del rectángulo (4).
     return:
     Number: area del rectángulo """
     return (base * altura)
 
rectangle = [7, 8]
area(*rectangle) # Este operador desempaqueta la variable rectangulo
