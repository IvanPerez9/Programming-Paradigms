import random

class SuperHeroe():

    def __init__(self, nombre, nacionalidad, estatura, peso, apodos = set() , poderes = set()):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        if len(apodos) == 0:
            self.apodos = self.nombre
        else:
            self.apodos = apodos
        self.poderes = poderes

    def ganarApodos (self, apodo):
        self.apodos.add(apodo)

    def perderApodo (self, apodo):
        self.apodos.remove(apodo)

    def superRetirado (self):
        for i in range(0,len(self.apodos)):
            self.apodos.pop()
        self.ganarApodos(self.nombre)

    def referenciaApodos (self):
        print("Se ha vuelto a ver a " + random.sample(self.apodos , 1).pop() + " en Nueva York. " + random.sample(self.apodos, 1).pop() + " ha sido visto en bla bla")


super1 = SuperHeroe("Spiderman" , "EEUU" , "1,80" , "75" , {"El trepa muros" , "Spidey"} , {"Tela" , "Escalar"})
print(super1.apodos)
super1.ganarApodos("PruebaApodo")
print(super1.apodos)
super1.perderApodo("PruebaApodo")
print(super1.apodos)

super1.referenciaApodos()
print("--")
print(super1.apodos)
super1.superRetirado()
print(super1.apodos)