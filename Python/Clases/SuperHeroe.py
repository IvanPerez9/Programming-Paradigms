'''
Created on 20 nov. 2018

@author: Iván
'''
import random

class Heroe(object):
    '''
    classdocs
    '''


    def __init__(self, nombre, nacionalidad, estatura, peso, apodos = set(),poderes=[]):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.apodos = apodos #FrozenSet ?? 
        self.poderes = poderes
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        
        if len(self.apodos) < 1 :
            self.apodos = {nombre}
        
    #Funciones de añadir y eliminar apodos, si se me queda vacio tiene que ser el nombre
    # Funcion que me pidan los apodos de un super heroe, pillar toda la lista de apodos y usar pop()
    
    # Variable privada con dos guiones bajos __ 
    
    def añadirApodo(self, apodo):
        #self.apodos.add(apodo) Esto vale
        self.apodos |= {apodo}
        #self.apodos = self.apodos.union({apodo}) LO MISMO
        
    def eliminarApodo(self,apodo):
        self.apodos -= {apodo}
        if len(self.apodos) < 1:
            self.apodos = {self.nombre}
    
    def retirar (self):
        for a in self.apodos:
            self.apodos.remove(a)
        #Se puede poner solo la ultima linea
        self.apodos = {self.nombre}
    
    def apodosSuper (self):
        self.apodos.pop()
        
    
    def store (self):
        with open("sh.txt" , "w" ) as f:
            f.write("nombre: " + self.nombre + "\n")
            f.write("nacionalidad: " + self.nacionalidad + "\n")
            f.write("estatura: " + self.estatura + "\n")
            f.write("peso: " + self.peso + "\n")
            f.write("poderes: ")
            for p in self.poderes:
                f.write(p + " ")
            f.write("\n")
            f.write("apodos: ")
            for p in self.apodos:
                f.write(p + " ")
                
    def store2 (self):
        with open("sh.txt" , "w" ) as f:
            f.write(self.nombre + "/")
            f.write(self.nacionalidad + "/")
            f.write(self.estatura + "/")
            f.write(self.peso + "/")
            f.write("poderes: ")
            for p in self.poderes:
                f.write(p + "/")
            f.write(p + "/")
            f.write("apodos: ")
            for p in self.apodos:
                f.write(p + "/")
                
    def store3 (self):
        with open ("sh.txt", "w") as f:
            f.write(self.nombre + "\n")
            f.write(self.nacionalidad + "\n")
            f.write(self.estatura + "\n")
            f.write(self.peso + "\n")
            for p in self.poderes:
                f.write(p + " ")
            f.write(self.apodo + "\n")
            for a in self.apodo:
                f.write(a + " ")
            
    def load1 (self):
        #Si quiero comprobar la parte de la izquierda coincide, pues voy guardando en un diccionario 
        with open("prueba.txt" , "r") as f:
            line = f.readline()
            self.nombre = line.split(":") [1] [1:] # El segundo corchete por quitar el primer espacio en blanco, como hacer trim()
            line = f.readline()
            self.nacionalidad = line.split(":") [1] [1:] #El primer corchete por quedarte la parte derecha del split()
            line = f.readline()
            self.altura = line.split(":") [1] [1:]
            line = f.readline()
            self.peso = line.split(":") [1] [1:] 
            line = f.readline()
            self.poderes = line.split(":") [1].split() #Divido la lista de poderes por espacios
            
    def load2 (self):
        with open ("sh.txt" , "r") as f:
            line = f.readline()
            l = line.spli("/")
            self.nombre = l[0]
            self.nacionalidad = l[1]
            self.altura = l[2]
            self.peso = l[3]
            self.poderes = l[4].split()
            self.apodos = set(l[5].split())
            
    def load3 (self):
        with open ("sh.txt" , "r") as f:
            line = f.readline()
            l = line.spli("/")
            self.nombre = l[0]
            self.nacionalidad = l[1]
            self.altura = l[2]
            self.peso = l[3]
            self.poderes = l[4].split()
            self.apodos = set(l[5].split())
            
    def load4(self):
        with open("SuperHeroes.txt","r") as f :
            self.nombre=f.readline()
            self.nacionalidad = f.readline()
            self.estatura = f.readline()
            self.__peso = f.readline()
            self.poderes = f.readline().split
            self.poderes = set(f.readline().split())
             
        
def noticia (superheroe):
    apodos = superheroe.apodos
    print("Se ha vuel a ver a " + apodos.pop() + " en nueva york, " + apodos.pop() + "ha sido visto en Central Park")
  
def noticia2 (superheroe):      
    apodos = superheroe.apodos
    print("Se ha vuel a ver a " + random.sample(apodos , 1).pop() + " en nueva york, " + apodos.pop() + "ha sido visto en Central Park")
    #El random sample te saca una lista de 1 elemento, usando pop o [0]
    # Choice no vale porque requiere indexacion, no vale con set    
        
class sh:
    def __init__(self,nombre, iterable):
        self.nombre = nombre
        self.poderes = []
        for i in iterable:
            self.__añadir(i)
        
    def añadir (self,poder):
        self.poderes.append(poder)
        
    __añadir = añadir # Para poder hacer override, dejamos una como privada, y la igualamos a la funcion fuera del constructor como publica
    #Rpoteger como prevada
        
        
class villano (sh):
    def añadir(self, poder,coste):
        self.poderes.append((poder,coste))
        
        
lex = villano("Lex Luthor" , [("Rico", 0) , ("Listo" , 1)])
print(lex.poderes)
