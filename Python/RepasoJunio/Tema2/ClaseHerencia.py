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
import random

class Persona:

    def __init__(self, nombre, estatura, peso, nacionalidad):
        self.nombre = nombre;
        self.estatura = estatura;
        self.peso = peso;
        self.nacionalidad = nacionalidad;


class SuperPersona (Persona):

    def __init__(self,nombre,estatura,peso,nacionalidad, poderes = set() , apodos = set()):
        super(SuperPersona, self).__init__(nombre,estatura,peso,nacionalidad)
        self.poderes = poderes
        self.apodos = apodos

    def actuar (self, ciudad, verbo):
        a = self.apodos.pop();
        print(a , verbo + "la ciudad " + ciudad)
        self.apodos.add(a)

    def descendencia (self, pareja):
        """
        - 50% de heredar el poder de cada padre
        - Probabilidad final depende del numero de poderes del hijo
        """
        nombre = self.nombre + pareja.nombre;
        nacionalidad = self.nacionalidad + pareja.nacionalidad
        peso = (self.peso + pareja.peso) / 2
        estatura = (self.estatura + pareja.estatura) / 2
        apodos = self.apodos + pareja.apodos
        poderes = set()
        union = set().union(self.poderes, pareja.poderes)
        for e in union:
            if e in self.poderes and e in pareja.poderes:
                poderes.add(e)
            elif e in self.poderes and e not in pareja.poderes:
                num = random.randint(0,1)
                if round(num) == 1:
                    poderes.add(e)
            elif e not in self.poderes and e in pareja.poderes:
                num = random.randint(0,1)
                if round(num) == 1:
                    poderes.add(e)

        salida = SuperPersona(nombre,nacionalidad,peso,estatura,poderes, apodos)
        return salida


class Villano(SuperPersona):

    def actuar(self, ciudad):
        super(Villano, self).actuar(ciudad, "ataca")
        # Super y ctrl mas espacio, call


p= Persona("Pepe" , 1.8 , 75, "ESP")
print(p.nombre)
p2 = SuperPersona("Pepito" , 1.8 , 80, "ITA", ["Escalar", "Super Salto"], ["Pep"] )
print(p2.nombre)
print(p2.poderes)
p3 = SuperPersona("WonderWoman" , 1.8 , 80, "ESP", ["Super Fuerza", "Escalar"] , ["WW"] )
print(p3.nombre)
print(p3.poderes)
print("---")
p4 = p3.descendencia(p2)
print(p4.nombre)
print(p4.poderes)