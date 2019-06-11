import random

class Persona ():

    def __init__(self, nombre, estatura, peso , nacionalidad):
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.nacionalidad = nacionalidad

class superPersona (Persona):

    def __init__(self, nombre, estatura, peso , nacionalidad, poderes = [] , apodos = set()):
        super(superPersona, self).__init__(nombre, estatura, peso ,nacionalidad)
        self.poderes = poderes
        self.apodos = apodos

    def actuar (self, ciudad , verbo):
        print(random.sample(self.apodos, 1).pop() +" " +  verbo + " la ciudad de " + ciudad )

    def descendencia (self, pareja):
        nombre = self.nombre + pareja.nombre
        estatura = (self.estatura + pareja.estatura) / 2
        peso = (self.peso + pareja.peso) / 2
        if self.nacionalidad == pareja.nacionalidad:
            nacionalidad = self.nacionalidad
        else:
            nacionalidad = self.nacionalidad + pareja.nacionalidad

        apodos = self.apodos + pareja.apodos

        poderes = set()
        union = set().union(self.poderes, pareja.poderes)
        for i in union:
            if i in self.poderes and i in pareja.poderes :
                poderes.add(i)
            elif i in self.poderes and i not in pareja.poderes:
                n = random.random()
                if round(n) == 1:
                    poderes.add(i)
            elif i not in self.poderes and i in pareja.poderes:
                n = random.random()
                if round(n) == 1:
                    poderes.add(i)

        ret = superPersona(nombre, estatura, peso, nacionalidad, poderes, apodos)
        return ret
    
class Villano (superPersona):
    
    def actuar(self, ciudad , verbo):
        super(Villano, self).actuar(ciudad, "ataca")

class Heroe (superPersona):
    
    def actuar(self, ciudad , verbo):
        super(Heroe, self).actuar(ciudad , "salva")

p= Persona("Pepe" , 1.8 , 75, "ESP")
print(p.nombre)
p2 = superPersona("Pepito" , 1.8 , 80, "ITA", ["Escalar", "Super Salto"], ["Pep"] )
print(p2.nombre)
print(p2.poderes)
p3 = superPersona("WonderWoman" , 1.8 , 80, "ESP", ["Super Fuerza", "Escalar"] , ["WW"] )
print(p3.nombre)
print(p3.poderes)
print("---")
p4 = p3.descendencia(p2)
print(p4.nombre)
print(p4.poderes)

print("--")
p5 = Villano("PepeMalo",  1.8 , 80, "ITA", ["Escalar", "Super Salto"], ["Pep"] )
p5.actuar("NY", "aa")