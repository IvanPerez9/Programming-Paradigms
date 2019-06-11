import  random

class SuperHeroe ():

    def __init__(self, nombre ,nacionalidad, peso , estatura, apodos = set() , poderes = set()):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.peso = peso
        self.estatura = estatura
        if len(apodos) == 0:
            self.apodos = self.nombre
        else:
            self.apodos = apodos

        self.poderes = poderes

    def ganarApodos (self, apodo):
        self.apodos.add(apodo)

    def perderApodo (self, apodo):
        self.apodos.remove(apodo)

    def jubilarse (self):
        for i in range(0, len(self.apodos)):
            self.apodos.pop()
        self.apodos.add(self.nombre)

    def referenciaSuper (self):
        print("Se ha vuelto a ver a " +  random.sample(self.apodos , 1).pop() +  " en Nueva York," + random.sample(self.apodos , 1).pop() + " ha sido visto en Central Park," + random.sample(self.apodos , 1).pop() + " gritaban los transeúntes.")
        # Usar pop() para sacar un elemento al que concatenar

    def registrarSuper (self) :
        with open("FicheroPruebaHerencia.txt" , "w") as f: # Existe el "a" para editar
            f.write("Nombre: " + self.nombre + "\n")
            f.write("Nacionalidad: " + self.nacionalidad + "\n")
            f.write("Estatura: " + self.estatura + "\n")
            f.write("Peso: " + self.peso + "\n")
            f.write("Apodos: ")
            for i in self.apodos :
                f.write(i + " ")
            f.write("\n")
            f.write("Poderes: ")
            for i in self.poderes :
                f.write(i + " ")

    def cargarBBDD (self):
        with open("FicheroPruebaHerencia.txt" , "r") as f:
            line = f.readline().split(": ")
            self.nombre = line[1:]
            line = f.readline().split(": ")
            self.nacionalidad = line[1:]
            line = f.readline().split(": ")
            self.estatura = line[1:]
            line = f.readline().split(": ")
            self.peso = line[1:]
            line = f.readline().split(": ")
            self.apodos = line[1].split(" ")
            line = f.readline().split(": ")
            self.poderes = line[1].split(" ")


if __name__ == '__main__':

    super1 = SuperHeroe("Spiderman" , "EEUU" , "1,80" , "75" , {"Spidey" , "TrepaMuros"} , {"Telarana" ,"Trepar"})

    print(super1.apodos)
    super1.ganarApodos("Prueba")
    super1.perderApodo("TrepaMuros")
    print(super1.apodos)
    #super1.jubilarse()
    #print(super1.apodos)
    super1.referenciaSuper()
    print(super1.apodos)

    super1.registrarSuper()
    super2 = SuperHeroe("" , "EEUU" , "1,80" , "75" , {} , {})
    super2.cargarBBDD()
    print(super2.poderes)
    print(super2.nombre)
