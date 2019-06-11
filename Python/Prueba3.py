
# Poder sobrescribir sin afectar al metodo que sobreescribo

class SuperHeroe:
    def __init__(self, nombre, iterable):
        self.nombre = nombre
        self.poderes = []
        self.__añadirPoderes(iterable)

    def añadirPoderes(self, iterable):
        for e in iterable:
            self.poderes.append(e)

    __añadirPoderes = añadirPoderes


class Villano(SuperHeroe):
    def añadirPoderes(self, poderes, costes):
        for e in zip(poderes, costes):
            self.poderes.append(e)


v = Villano('Lex Luthor', [('rico', 0), ('listo', 10)])
print(v.poderes)