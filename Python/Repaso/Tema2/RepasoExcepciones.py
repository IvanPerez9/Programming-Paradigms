'''
Created on 25 dec. 2018

@author: Iván


'''

"""
La función input muestra un mensaje que se pasa por parámetro
y espera a que el usuario introduzca un dato por teclado. Crear
una función que se asegure que el usuario introduce un entero
(avisando cada vez que se equivoque).
"""

#Al castear a int si lo haces mal sale "ValueError" asi sabes el tipo de excepcion que recoger
def numero ():
    try:
        while True:
            n = int(input("Introduce un numero: "))
            break;
    except ValueError:
        print("No ha introducido un numero")

numero()

"""
Proteger la función que carga el registro de héroes para que
avise si el fichero no existe (en lugar de fallar).
"""

#En el caso de que exista el fichero
def fichero ():
    try:
        with open("File.txt", "r") as f:
            line = f.readline()
            line.capitalize()
    except FileNotFoundError:
        print("Fichero no encontrado")


"""
Implementar nuestra propia función get, que recibe un
diccionario, una clave y un elemento. 
Devuelve el valor asociado a la clave, o elemento si la clave no está en el diccionario.
"""

def getPropia (diccionario, clave, e):
    try:
        print( diccionario[clave])
    except KeyError:
        print("No existe esa clave, devuelvo el elemento: " + str(e))


d = {"Uno" : 1 , "Dos" : 2 , "Tres" : 3}

getPropia(d, "Uno" , "Prueba")
getPropia(d , "Cuatro" , "Prueba")
