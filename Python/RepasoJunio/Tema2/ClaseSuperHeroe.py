"""
   Crear clase superheroe con nombre, apodos, nacionalidad, estatura, peso y poderes.

   Un superheroe tiene 1 o más apodos, si tiene 0 entonces será su propio nombre

   Metodos para ganar y perder apodos. Si se retira pierde todos los apodos

   Funcion que haga referencia a un SH por sus distintos apodos -> Frase Spiderman
   """

import random

class superHeroe:

    def __init__(self, nombre , nacionalidad, estatura, peso, apodos = set() , poderes = set()):
        self.nombre = nombre;
        self.nacionalidad = nacionalidad;
        self.estatura = estatura;
        self.peso = peso
        self.apodos = apodos
        self.poderes = poderes

        if len(self.apodos) == 0:
            self.apodos = {nombre}

    def ganarApodos (self,apodo):
        self.apodos.append(apodo)

    def perderApodo (self,apodo):
        self.apodos.remove(apodo)

    def retirado (self):
        while (len(self.apodos) != 0):
            self.perderApodo(self.apodos[0])

    def escribirApodos (self):
        print("Se ha vuelto a ver a " + self.apodos.pop() + " por la ciudad" )

    """
    Base de datos de superheroes

    Funcion para registrar en un fichero a nuestros superheroes -> Entrada Salida

    Funcion para cargar nuestra coleccion de superheroes -> Entrada salida

    """

    """
    Reimplementar la función que hacia uso de los apodos de un
    héroe para mostrar un mensaje usando el módulo random.
    """

    def escribirBBDD (self):
        with open("FicheroRepaso.txt", "w") as f:
            f.write("Nombre: " + self.nombre + "\n")
            f.write("Nacionalidad: " + self.nacionalidad + "\n")
            f.write("Estatura: " + self.estatura + "\n")
            f.write("Peso: " + self.peso + "\n")
            f.write("Apodos: ")
            for i in self.apodos:
                f.write( i+ " ")
            f.write("\n")
            f.write("Poderes: ")
            for i in self.poderes:
                f.write(i + " ")

    def leerBBDD (self):
        with open("FicheroRepaso.txt" , "r") as f:
            line = f.readline()
            self.nombre = line.split(":")[1:]
            line = f.readline()
            self.nacionalidad = line.split(":")[1:]
            line = f.readline()
            self.estatura = line.split(":")[1:]
            line = f.readline()
            self.peso = line.split(":")[1:]
            line = f.readline()
            self.apodos = line.split(":")[1:].split()  # Los espacios en blanco
            line = f.readline()
            self.poderes = line.split(":")[1:].split()


    def escribirApodos2 (self):
        print("Se ha vuelto a ver a " + random.sample(self.apodos , 1).pop() + " por la ciudad" )

super = superHeroe("Spiderman" , "EEUU" , "1,80" , "80" , ["ae"] , ["Tela"])
print(super.apodos)
super.ganarApodos("Spidey")
print(super.apodos)
super.escribirApodos()
super.escribirApodos2()
super.retirado()
print(super.apodos)

super2 = superHeroe("Spiderman" , "EEUU" , "1,80" , "80" , ["Spi"] , ["Tela"])
super2.escribirBBDD()