
# Clase morse con metodos codificar y descodificar

class Morse(object):

    def __init__(self):

        self.str2morse = {' ':' ','A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--',
                          'H': '....', 'I': '..',
                          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
                          'p': '.--.', 'Q': '--.-',
                          'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..'}

        self.morse2str = {' ':' ','A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--',
                          'H': '....', 'I': '..',
                          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
                          'p': '.--.', 'Q': '--.-',
                          'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..'}


    # Metodo para pasar de str a morse
    def codificar (self, cadena):
        cadenaResult = ""
        for i in cadena.upper():
            cadenaResult += self.str2morse[i] + ''

        return cadenaResult

    # Metodo para pasar de morse a str
    def descodificar (self, cadena):
        cadenaResult = ""
        for i in cadena:
            cadenaResult += self.morse2str[i] + ''

        return cadenaResult


nuevaCadena = Morse()

print(nuevaCadena.codificar("Hola que tal"))