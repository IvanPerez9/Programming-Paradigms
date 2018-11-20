'''
Created on 20 nov. 2018

@author: Iván
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, nombre, apodo,poder, nacionalidad, estatura, peso):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.apodos = {apodo} #FrozenSet ?? 
        self.poderes = {poder}
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        
    #Funciones de añadir y eliminar apodos, si se me queda vacio tiene que ser el nombre
    # Funcion que me pidan los apodos de un super heroe, pillar toda la lista de apodos y usar pop()
    
    def añadirApodo(self, apodo):
        self.apodos.add(apodo)
        
    def eliminarApodo(self,apodo):
        if not self.apodos:
            self.apodos = {self.nombre}
        else:
            self.apodos.remove(apodo)
    
    def apodosSuper (self):
        self.apodos.pop()
            