'''
Created on 27 nov. 2018

@author: Iván

'''

import random

class Persona(object):
    '''
    classdocs
    '''


    def __init__(self, nombre, estatura, peso, nacionalidad):
        '''
        Constructor
        '''
        self.nombre = nombre;
        self.estatura = estatura;
        self.peso = peso;
        self.nacionalidad = nacionalidad;
        

class SuperPersona(Persona):
    
    def __init__(self, nombre, estatura, peso, nacionalidad,poderes = [],apodos = []):
        super(SuperPersona,self).__init__(nombre, estatura, peso, nacionalidad)
        self.poderes = poderes
        self.apodos = apodos
        
    def acturar (self,ciudad,verbo):
        a = self.apodos.pop()
        print(a, verbo, "la ciudad de " , ciudad)
        self.apodos.add(a)
        
    def descendencia (self,pareja):
        nombre = self.nombre + pareja.nombre
        estatura = self.estatura + pareja.nombre
        peso = self.peso + pareja.nombre
        nacionalidad = self.n + pareja.nombre
        
        poderes = set()
        u = self.poderes | pareja.poderes ## Union de los poderes
        for p in u:
            prob = 0 
            if p in self.poderes and p in pareja.poderes:
                prob = 1
            else:
                prob = .5
            pf = prob / max (len(poderes),1) #Probabilidad entre el numero maximo de los poderes, el 1 para evitar que rea 1
            if random.random() <= pf: #Random de 0 a 1 , por eso esas probabilidades
                poderes.add(p)
        
        return SuperPersona(nombre,estatura,peso,nacionalidad, poderes )
    
class SuperHeroe (SuperPersona):
    
    def actuar (self,ciudad):
        super(SuperHeroe,self).actuar(ciudad, "salva")

class SuperVillano (SuperPersona):
    
    def actuar (self,ciudad):
        super(SuperHeroe,self).actuar(ciudad, "ataca")
        
p= Persona("Pepe" , 1.8 , 75, "ESP")
print(p.nombre)
p2 = SuperPersona("Pepito" , 1.8 , 80, "ITA" )
print(p2.nombre)
