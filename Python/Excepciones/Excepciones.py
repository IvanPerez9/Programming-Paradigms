'''
Created on 27 nov. 2018

@author: Iván


'''

# Crear una función que se asegure que el usuario introduce un entero 

def asegurar ():
    while True:
        try:
            x = int(input("Introduce un numero: "))
            break;
        except ValueError:
            print("Error")
            
asegurar()

# Tres formas de resolver el otro, con un if o con un try mirando si hay division por 0

# El if siempre va a comprobar el if , con lo cual no es muy optimo
# Haciendo con un max, tendria otro if asi que... El max len que tenemos

#Con excepciones, no hay sobrecarga si no existe el fallo. Es lo que menos trabajo usa.

"""
Implementar nuestra propia funcion get, que recibe un
diccionario, una clave y un elemento. Devuelve el valor asociado
a la clave, o elemento si la clave no está en el diccionario.
"""

def get (diccionario, clave, elemento):
    try:
        return diccionario[clave]
    except KeyError:
        return elemento
        
print(get({1:"hola"},1,2))

"""
Decvimal  se tiene que pasar como string, ya que si no se pasa como float y no se puede rep`resentar
"""