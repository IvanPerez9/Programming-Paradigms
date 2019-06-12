"""
Escribe una función en Python que recibe 2 parametros, la ruta a dos ficheros de texto.
 - El primer fichero es una lista de "palabras de interes" separadas por espacios.
 - El segundo fichero será un fichero de texto normal con frases y parrafos.

 Se pide crear una función que devuelva en una colección cuales (si hay alguna) de las palabras de
  interes aparecen en el segundo fichero y tambíen devolverá otra colección en la que
 indique cuantas veces aparece cada palabra de interes. Será necesario documentar la función/es creada/s.
"""

def abrirFichero (fichero):
    """
    Funcion que sirve para abrir el fichero en modo lectura -> Para ambos tipos de ficheros
    :param fichero:
    :return:
    """
    l = list()
    with open(fichero , "r") as f:
        for line in f:
            for palabra in line.split():
                l.append(palabra)
    return l

# Palabra fichero1 clave, que aparecen en el fichero 2
def palabrasAparecen (fichero1 , fichero2):
    l1 = abrirFichero(fichero1) #Palabras clave
    l2 = abrirFichero(fichero2) # Texto normal
    salida = set()

    for i in l1:
        if i in l2:
            salida.add(i)

    return salida

# Palabras que aparecen y el numero de veces que aparecen
def palabrasNumeroDiccionario (fichero1, fichero2):
    l1 = abrirFichero(fichero1)  # Palabras clave
    l2 = abrirFichero(fichero2)  # Texto normal
    dic = dict()

    for i in l2:
        if i in l1:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        else:
            dic[i] = 0

    return dic


if __name__ == '__main__':
    fichero1 = "fichero1.txt"
    fichero2 = "fichero2.txt"
    print(abrirFichero(fichero2))

    print(palabrasAparecen(fichero1, fichero2))
    print(palabrasNumeroDiccionario(fichero1, fichero2))