'''
Created on 20 nov. 2018

@author: Iván
'''

class Morse(object):
    '''
    classdocs
    '''

    """    
     INVERTIR
    for k,v in self.diccionario:
        self.diccionario[v] = k
    """

    #No buscar por valor en un diccionario

    def __init__(self):
        '''
        Constructor
        '''
        self.morse2str = {' ':' ','.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--': 'M',
                           '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '-.': 'N', '--.--': 'Ñ', '---': 'O', '.--.': 'p',
                            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..--': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                             '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', ':...--': '3', '....-': '4', '.....': '5', '-....': '6',
                              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '-.-.--': ',', '..--..': '?', '.-..-.': '"', '--..--': '!'}
        self.str2morse = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
         '!': '--..--'}


    #Lo guarod en r que es un string para poder imprimirlo 
    def codificar (self,text):
        r = '';
        for c in text:
            r += self.morse2str[c] + ' '
            
    def decodificar (self,morse):
        r = '';
        for c in morse.split(): #Diferencio las cadenas de puntos y rayas de morse por los espacios
            r += self.str2morse[c] + ' '
        
        
        
        
        
        
        
        