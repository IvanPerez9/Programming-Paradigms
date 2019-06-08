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


    def registrarHeroes (self):
        with open("FicheroRepasoHeroes" , "w") as f:
            f.write("Nombre: " + self.nombre + "\n")
            f.write("Nacionalidad: " + self.nacionalidad + "\n")
            f.write("Estatura: " + self.estatura + "\n")
            f.write("Peso: " + self.peso + "\n")
            f.write("Apodos: ")
            for i in self.apodos:
                f.write(i + " ")
            f.write("\n")
            f.write("Poderes: ")
            for i in self.poderes:
                f.write(i + " ")


    def cargarHeroe (self)  :
        with open("FicheroRepasoHeroes" , "r") as f:
            line = f.readline().split(": ")
            self.nombre = str(line[1:])
            line = f.readline().split(": ")
            self.nacionalidad = line[1:]
            line = f.readline().split(": ")
            self.estatura = line[1:]
            line = f.readline().split(": ")
            self.peso = line[1:]
            line = f.readline().split(": ")
            self.apodos = line[1].split(" ")
            line = f.readline()
            self.poderes = line.split(": ")[1].split(" ")


super1 = SuperHeroe("Spiderman" , "EEUU" , "1,80" , "75" , {"El trepa muros" , "Spidey"} , {"Tela" , "Escalar"})
print(super1.apodos)
super1.ganarApodos("PruebaApodo")
print(super1.apodos)
super1.perderApodo("PruebaApodo")
print(super1.apodos)

super1.referenciaApodos()
print("--")
#super1.registrarHeroes()
super1.cargarHeroe()
print(super1.nombre)
print(super1.poderes)
print(super1.apodos)