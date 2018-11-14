'''
Created on 14 nov. 2018

@author: Iván
'''

# Es como un saco de elementos
#Unica manera de hacerlo vacio es con el constructor, no se puede porner {} 
# No es hasheable, no puede tener set de set

# Reimplementar  la funcion de los 100 primeros primos haciendo uso de conjuntos

def isPrimo (num, p):
    for e in p:
        if num % e == 0:
            return False
    return True

def primos ():
    """
    Mirar los anteriores primos. Tener un conjunto de primos
    return : Devolver la lista de primos
    """
    p = set()
    
    for i in range(2,100) :
        if isPrimo(i, p) :
            p.add(i)
    return p
        
print(primos())      


def digitos (num):
    #Transformar el numero en un string y coger la posicion que quieras
    # Print tiene un parametro end con el que poner " " para que los ponga seguidos
    # Se puede hacer con div y mod
    # Insert inserta por le principio y append por el final
    l = []
    while num :
        l.insert(0 , num %10)
        num //= 10
    print(l)

def digitos2 (n):
    l = []
    for e in str(n):
        l.append(int(e))
    print(l)
    
digitos(567)
digitos2(345)

def union (c1, c2):
    """
    Union de conjuntos
    """
    c = set()
    for e in c1 :
        c.add(e)
    for i in c2 :
        c.add(i)
    return c 

def interseccion (c1, c2):
    """ 
    Los elementos qu estan en los dos conjuntos
    """
    c = set()
    for e in c1 :
        if e in c2 :
            c.add(e)
    
    return c 

def difference (c1 ,c2):
    """
    LA diferencia en tre los dos
    """
    c = set()
    for e in c1 : 
        if e not in c2 :
            c.add(e)
    return c 

def copia (c):
    c2 = set()
    for e in c:
        c2.add(e)
        
    return c2


# Funcion cubifinito 
# Si al elevar al cubo sus digitos al sumarlos es 1 u otro cubifinito

def cubifinitos (n, c = set()): 
    cf = {1} # Conjunto de cubifinitos
    c = set() # Lista de candidatos
    l = digitos(n)
    s = 0
    for e in l:
        s += e ** 3
    if s in cf :
        #cf.add(n) Si quieres conservar a los candidatos
        return True
    elif s in c :
        return False
    else :
        c.add(s)
        cubifinitos(s, c)
        

#cubifinitos(11)
    


"""
FORCESET
"""

# LE paso una lista de parejas de positivos y negativos, todos tienen pareja menos 1 , encontrar y devolver cual es

# Si sumas ylos numeros te queda solo el que esta solo
#Si no esta en el conjunto lo meto pero invertido, y cuando encuentre el invertido lo saco. Solo me queda el que no tiene
def opositepair(l):
    c = set()
    for e in l:
        if e not in c :
            c.add(-e)
        else:
            c.remove(e)
    return -c.pop()
    
l = [3,5,-7,-9,-3,7,9]
print(opositepair(l))
    
# Crea un funcion que devuelve el numero no repetido

def single (l):
    s = 0
    for e in l:
        s ^= e
    return s

l = [1,2,3,4,1,2,3]
print(single(l))

#Dividir un conjunto entre pares e impares

def evensplit (c1):
    e = set()
    o = set()
    for i in c1:
        if i % 2 == 0:
            e.add(i)
        else:
            o.add(i)
    return e,o

print(evensplit([1,2,3,4]))
    