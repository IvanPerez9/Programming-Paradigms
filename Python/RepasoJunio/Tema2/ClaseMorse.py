"""
Implementa una clase morse con las funciones de codificar y decodificar
para pasar un String a Morse y viceversa
"""

class Morse:

    def __init__(self):

        self.morse2str = {' ': ' ', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--': 'M',
                          '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '-.': 'N', '--.--': 'Ñ',
                          '---': 'O', '.--.': 'p',
                          '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..--': 'U', '...-': 'V', '.--': 'W',
                          '-..-': 'X', '-.--': 'Y',
                          '--..': 'Z'}

        self.str2morse = {' ':' ','A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--',
                          'H': '....', 'I': '..',
                          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
                          'p': '.--.', 'Q': '--.-',
                          'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..'}


    def codificar (self,cadena):
        resultado = ''
        for i in cadena.upper():
            resultado += self.str2morse[i] + ' '

        return resultado

    def descodificar (self,cadena):
        resultado = ''
        for i in cadena:
            resultado += self.morse2str[i] + ''

        return resultado

nuevaCadena = Morse();

print(nuevaCadena.codificar("ABC"))

