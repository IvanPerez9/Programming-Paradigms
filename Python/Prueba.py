"""
Archivo para ir probando hasta el examen
"""

import random
import statistics
import datetime

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

def noticia2 (superHeroe):
    apodos = superHeroe.apodos
    print("Se ha vuelto a ver a " + random.sample(apodos , 1).pop() + " en NY, " + random.sample(apodos , 1).pop() + " ha sido visto en central park")


sM.ganarApodos("Kal El")
noticia(sM)
sM.ganarApodos("El hijo de Krypton" )
sM.ganarApodos("El hombre del mañana")
sM.ganarApodos("Avion")
print(sM.apodos)
print("-")
noticia2(sM)
noticia2(sM)
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

print("*******************************")
print(" ")

tipo = {"Casa" , "piso" , "caja carton"}
def inmobiliaria (tipo, precio):
    propiedad = []
    for i in range(10):
        propiedad.append((random.sample(tipo , 1)[0] , random.randint(10000 , precio)))
    return propiedad

salida = (inmobiliaria(tipo , 200000))
print(salida)


#Estafa cara o cruz

moneda = random.randint(0,1)

def lanzamiento ():
    moneda = random.randint(0, 1)
    if moneda == 1 :
        return "H"
    else:
        return "T"

def tirando (seq):
    lanzar = lanzamiento()
    while seq not in lanzar:
        lanzar += lanzamiento()

    return lanzar

print(tirando("HTH"))

def seq2 (seq1 , seq2):
    lanzar = lanzamiento()
    contador = 0
    while seq1 not in lanzar and seq2 not in lanzar:
        lanzar += lanzamiento()
        contador += 1
    if seq1 in lanzar:
        return seq1, contador
    else:
        return seq2, contador

ganador = (seq2("TTT" , "HHH"))
print("El ganador es: " + ganador[0] + " con " + str(ganador[1]) + " tiradas" )

#Fechas, 3 modulos datetime , time y date

def fechaGregoriano (fecha):
    return fecha.strftime("%j")

def inversaJ (fecha):
    return fecha.strptime ("365" , "%j")

date = datetime.date.today()
print(fechaGregoriano(date))

#Cumpleaños

def fechaAleatoria ():
    date = random.randint(1, 365)
    return datetime.datetime.strptime(str(date) , "%j")

print(fechaAleatoria())

def guardarFechas (fecha):
    lista = list()
    contador = 0
    while fecha not in lista:
        lista.append(fechaAleatoria())
        contador += 1

    return contador

datee = fechaAleatoria()
print(guardarFechas(datee))

#RE


