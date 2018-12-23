'''
Created on 23 dec. 2018

@author: Iván
'''

class SuperHeroe (object):

    """
    Crear clase superheroe con nombre, apodos, nacionalidad, estatura, peso y poderes.

    Un superheroe tiene 1 o más apodos, si tiene 0 entonces será su propio nombre

    Metodos para ganar y perder apodos. Si se retira pierde todos los apodos

    Funcion que haga referencia a un SH por sus distintos apodos -> Frase Spiderman
    """

    def __init__(self, nombre, nacionalidad, estatura, peso, apodos = set() , poderes = set()):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        self.apodos = apodos
        self.poderes = poderes

        if len(self.apodos) < 1:
            self.apodos = {nombre}

    def añadirApodo (self,apodo):
        self.apodos.append(apodo)
        #self.apodos |= {apodo}

    def quitarApodo (self,apodo):
        self.apodos.remove(apodo)
        #self.apodos -= {apodo}
        if len(self.apodos) < 1:
            self.apodos = {self.nombre} #Ojo pasar a SET

    def heroeRetirado (self):
        for i in range(len(self.apodos)):
            self.apodos.remove(i)

        if len(self.apodos) < 1 :
            print("Retirado no tiene apodos")
            self.apodos = {self.nombre}

    def obtenerApodo (self):
        self.apodos.pop()

    #Funcion que muestre una noticia por distintos apodos


superheroe = SuperHeroe("Spiderman" , "EEUU" , "1,80", "80kg" , ["Maquina","Spidey"], [])
superheroe.quitarApodo("Maquina")
superheroe.añadirApodo("Spiderman")
for i in range(len(superheroe.apodos)):
    print(superheroe.apodos[i])

print("---")


def noticia(superheroe):
    apodos = superheroe.apodos
    print("Se ha vuel a ver a " + apodos.pop() + " en nueva york, " + apodos.pop() + " ha sido visto en Central Park")

noticia(superheroe)