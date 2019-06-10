class mamifero ():
    def __init__(self, nombre):
        self.nombre = nombre

class vertebrado ():
    def __init__(self, tipo):
        self.tipo = tipo

class perrito (vertebrado):

    def __init__(self, nombre, tipo, tipoPerro):
        mamifero.__init__(self,nombre)
        vertebrado.__init__(self, tipo)
        self.tipoPerro = tipoPerro

p = perrito("Perro" , "tipo" , "peludo")
print(p.nombre)
print(p.tipo)
print(p.tipoPerro)