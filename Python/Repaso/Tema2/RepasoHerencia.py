'''
Created on 24 dec. 2018

@author: Iván

'''
import random
"""
Crear una jerarquia de clases que incluya
    - Persona: Nombre,Estatura,peso y nacionalidad
    - Super Persona: Lista de poderes, apodos
    - Super Heroe
    - Super Villano

Toda super persona tiene la funcion actuar, que recibe el nombre de una ciudad e imprime por 
pantalla un apodos y la frase "salva la ciudad de" o ataca en funcion si es un heroe o villano

Cuando una superpersona tiene hijos, esto heredan.
    - 50% de heredar el poder de cada padre
    - Probabilidad final depende del numero de poderes del hijo 
"""

class Persona (object):
    """
    Clase persona
    """
    def __init__(self,nombre,estatura,peso,nacionalidad):
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.nacionalidad = nacionalidad

class SuperPersona (Persona):
    """
    Clase SuperPersona: Hereda de Persona
    """
    def __init__(self,nombre,estatura,peso,nacionalidad,poderes,apodos):
        super(SuperPersona,self).__init__(nombre,estatura,peso,nacionalidad)
        self.poderes = poderes
        self.apodos = apodos

    def actuar (self, nombreCiudad, verbo):
        a = self.apodos.pop()
        print(a, verbo, "la ciudad de ", nombreCiudad)
        self.apodos.add(a)

    # Cuando tiene hijos la superPersona

    def descendencia (self,pareja):
        """
        :param pareja: Otra persona o superpersona
        :return: Un superHeroe
        """

        nombre = self.nombre + pareja.nombre
        estatura = (int(self.estatura + pareja.estatura)) // 2
        peso = (int(self.peso + pareja.peso)) // 2
        nacionalidad = self.nacionalidad + pareja.nacionalidad
        apodos = str(self.apodos) + str(pareja.apodos)

        poderes = set()
        union = set().union(self.poderes, pareja.poderes) #Union de todos los poderes, casteo a set
        for e in union:
            prob = 0
            if e in self.poderes and e in pareja.poderes:
                prob = 1
            else:
                prob = .5
            pf = prob / max(len(poderes),
                            1)  # Probabilidad entre el numero maximo de los poderes, el 1 para evitar que rea 1
            if random.random() <= pf:  # Random de 0 a 1 , por eso esas probabilidades
                poderes.add(e)

        hijo = SuperPersona(nombre,estatura,peso,nacionalidad,poderes,apodos)

        return hijo

class SuperHeroe (SuperPersona):
    
    """
    Clase superHeroe y Villano, no necesito constuctor, usa el mismo que superPersona
    No tiene nada que sobrescribir
    
    Solo sobreescribe el metodo
    """
    
    def actuar(self, nombreCiudad):
        super(SuperHeroe, self).actuar(nombreCiudad," salva ")

class Villano (SuperPersona):
    
    def actuar(self, nombreCiudad):
        super(Villano, self).actuar(nombreCiudad, " actaca ")

#PRUEBA

p= Persona("Pepe" , 1.8 , 75, "ESP")
print(p.nombre)
p2 = SuperPersona("Pepito" , 1.8 , 80, "ITA", ["Escalar", "Super Salto"], ["Pep"] )
print(p2.nombre)
print(p2.poderes)
p3 = SuperPersona("WonderWoman" , 1.8 , 80, "ESP", ["Super Fuerza"] , ["WW"] )
print(p3.nombre)
print(p3.poderes)
print("--un")
p4 = p3.descendencia(p2)
print(p4.poderes)
print(p4.nombre)

#Mirar union,diferencia etc y la indexacion con set y diccionarios
