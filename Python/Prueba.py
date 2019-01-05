"""
Archivo para ir probando hasta el examen
"""

"""
Clase superHeroe
"""

class superHeroe (object):

    def __init__(self, nombre , nacionalidad,estatura,peso,apodos,poderes):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        self.apodos = apodos
        self.poderes = poderes

        if len(apodos) < 1 :
            self.apodos = nombre

    def ganarApodos (self, newApodo):
        self.apodos.append(newApodo)

    def quitarApodo (self, apodo):
        self.apodos.remove(apodo)

    def retirarse (self):
        while len(self.apodos) > 0:
            self.apodos.pop()

        if len(self.apodos) < 1 :
            self.apodos = {self.nombre}

    def darApodo (self):
        if len(self.apodos) > 0 :
            return self.apodos.pop()
        else:
            return self.nombre

    def almacenarSuper (self):
        with open("File.txt", "w") as f:
            f.write("Nombre: " + self.nombre + "\n")
            f.write("Nacionalidad " + self.nacionalidad + "\n")
            f.write("Altura " + self.estatura + "\n")
            f.write("Peso " + self.peso + "\n")
            f.write("Apodos " + "\n")
            for i in self.apodos:
                f.write( i + " ")
            f.write("Poderes " + "\n")
            for e in self.poderes:
                f.write(e + " ") #Separo por un espacion en blanco

    def cargarSuper (self, nombreArchivo):
        with open(nombreArchivo , "r") as f:
            line = f.readline()
            self.nombre = line.split(":") [1:]
            line = f.readline()
            self.nacionalidad = line.split(":")[1:]
            line = f.readline()
            self.estatura = line.split(":")[1:]
            line = f.readline()
            self.peso = line.split(":")[1:]
            line = f.readline()
            self.apodos = line.split(":")[1:].split()
            line = f.readline()
            self.poderes = line.split(":")[1:].split()

class Persona (object):

    def __init__(self, nombre, estatura, peso , nacionalidad):
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.nacionalidad = nacionalidad

class superPersona (Persona):

    def __init__(self, nombre, estatura, peso, nacionalidad ,poderes, apodos):
        super(superPersona, self).__init__(nombre,estatura,peso,nacionalidad)
        self.poderes = poderes
        self.apodos = apodos

    def actuar (self, nombreCiudad, verbo ):
        apodo = self.apodos.pop()
        print(apodo + verbo + " la " + nombreCiudad + " de ")
        self.apodos.append(apodo)

    def descendencia (self, pareja):
        nombre = self.nombre + pareja.nombre
        estatura = (int(self.estatura) + int(pareja.estatura))// 2
        peso = (int(self.peso) + int(pareja.peso)) // 2
        nacionalidad = str(self.nacionalidad) + str(pareja.nacionalidad)
        poderes = str(self.poderes.pop()) + str(pareja.poderes.pop())
        apodos = self.apodos.pop()

        hijo = superPersona(nombre,estatura,peso,nacionalidad,poderes,apodos)
        return hijo
    
class Villano (superPersona):
    
    def actuar (self, nombreCiudad):
        super(Villano, self).actuar(nombreCiudad , " ataca ")

class SuperHeroe2 (superPersona):
    
    def actuar (self, nombreCiudad):
        super(SuperHeroe2, self).actuar(self,nombreCiudad, " salva ")

sM = superHeroe("Superman" , "EEUU" , "1,80" , "78" , ["Hombre de Acero"] , ["Superfuerza" , "Volar"])

def noticia (superHeroe):
    print("Se ha vuelto a ver a " + superHeroe.darApodo() + " en NY, " + superHeroe.darApodo() + " ha sido visto en central park")

sM.ganarApodos("Kal El")
noticia(sM)
sM.ganarApodos("El hijo de Krypton" )
sM.ganarApodos("El hombre del mañana")
sM.ganarApodos("Avion")
print(sM.apodos)
noticia(sM)
sM.ganarApodos("El hijo de Krypton")
sM.retirarse()
noticia(sM)

print("----")

p= Persona("Pepe" , 1.8 , 75, "ESP")
print(p.nombre)
p2 = superPersona("Pepito" , 1.8 , 80, "ITA", ["Escalar", "Super Salto"], ["Pep"] )
print(p2.nombre)
print(p2.poderes)
p3 = superPersona("WonderWoman" , 1.8 , 65, "ESP", ["Super Fuerza"] , ["WW"] )
print(p3.nombre)
print(p3.poderes)
print("--un")
p4 = p3.descendencia(p2)
print(p4.peso)
print(p4.poderes)
print(p4.nombre)

