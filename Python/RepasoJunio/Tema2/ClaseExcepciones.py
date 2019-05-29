"""
La función input muestra un mensaje que se pasa por parámetro
y espera a que el usuario introduzca un dato por teclado. Crear
una función que se asegure que el usuario introduce un entero
(avisando cada vez que se equivoque).
"""

def introduceEntero ():
    try:
        while True:
            print("Introduzca un valor entero")
            n = int(input())
    except ValueError:
        print("No es un entero")

#introduceEntero()

"""
Proteger la función que carga el registro de héroes para que
avise si el fichero no existe (en lugar de fallar).
"""

def cargarFichero():
    try:
        with open("ficheronoexiste" , "r") as f:
            line = f.readline()
            print(line)
    except FileNotFoundError:
        print("Fichero no existe")

#cargarFichero()

"""
Implementar nuestra propia función get, que recibe un
diccionario, una clave y un elemento. 
Devuelve el valor asociado a la clave, o elemento si la clave no está en el diccionario.
"""

def funcionGet (diccionario, clave , elemento):
    try:
        print(diccionario[clave])
    except KeyError:
        print("No existe esa clave: " + elemento)

diccionario = {1:"uno" , 2:"dos"}
funcionGet(diccionario, 3 , "elem")