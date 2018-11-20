
'''Funcion que devuelve la inversa de un diccionario'''
agenda={'Luis' : 689332211, 'Maria': 753951456, 'Julio' : 147852654}
morse = {'A': '.-', 'B': "-...", 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'p': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': ':...--', '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '-.-.--', '?': '..--..', '"': '.-..-.',
         '!': '--..--'}


def inverso1 (dic):
    k=dic.keys()
    v=dic.values()
    d=dict(zip(v,k))
    print(d)

def inverso2 (dic):
    k = dic.items()
    d={}
    lista=[]
    for e in k:
        lista.append(e)
    lista=list(reversed(lista))
    for k, v in lista:#se pueden acceder asi a los elementos de la tupla
        d[k]=v

    print(d)

inverso1(morse)
inverso2(agenda)
