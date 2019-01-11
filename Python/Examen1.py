"""
Escribe una función en Python que recibe 2 parametros, la ruta a dos ficheros de texto.
 El primer fichero es una lista de "palabras de interes" separadas por espacios.
 El segundo fichero será un fichero de texto normal con frases y parrafos.
 Se pide crear una función que devuelva en una colección cuales (si hay alguna) de las palabras de
  interes aparecen en el segundo fichero y tambíen devolverá otra colección en la que
 indique cuantas veces aparece cada palabra de interes. Será necesario documentar la función/es creada/s.
"""

def palabrasInteres (file1 , file2):
    """
    Tiene los dos ficheros y busca las palabras del primero en el segundo. Si la encuentra la guarda junto a un contador
    :param file1:
    :param file2:
    :return: Devuelve tanto las palabras encontradas en una lista
    """
    l1 = abrirFichero(file1) #Palabras interesantes
    l2 = abrirFichero(file2) # Fichero de frases
    l = list()
    d = dict()
    for i in l1:
        for e in l2:
            for x in i:
                for y in e:
                    if x == y :
                        l.append(x)
    return l

def palabrasInteresDiccionario(file1 , file2):
    """
    Tiene los dos ficheros y busca las palabras del primero en el segundo. Si la encuentra la guarda junto a un contador
    :param file1:
    :param file2:
    :return: Devuelve un diccionario donde la clave es la palabra y el valor las veces que se ha repetido
    """
    l1 = abrirFichero(file1) #Palabras interesantes
    l2 = abrirFichero(file2) # Fichero de frases
    d = dict()
    for i in l1:
        for e in l2:
            for x in i:
                for y in e:
                    if x == y :
                        if not x in d:
                            d[x] = 1
                        else:
                            d[x] += 1
    return d



def abrirFichero (file):
    """
    Subprograma que me permite abrir un fichero sin preocupame de cerrarlo, y leer de el
    :param file:
    :return: Almacena en una lista todas las palabras del fichero
    """
    l = list()
    with open(file , "r") as f:
        l.append(f.readline().split())
    return l

if __name__ == '__main__':

    fichero1 = "fichero1.txt"
    fichero2 = "fichero2.txt"

    print(palabrasInteres(fichero1,fichero2))
    print(palabrasInteresDiccionario(fichero1,fichero2))