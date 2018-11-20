
#Reimplementar las funciones que cuentan caracteres y palabras

def caracteres (cadena):
    d = dict();
    for c in cadena:
        if c in d :
            d[c] += 1
        else:
            d[c] = 1
    return d 

print(caracteres("Holaaas"))

def caracteresReimplementacion (cadena):
    d = dict()
    for c in cadena:
        d[c] = d.get(c, 0) + 1 # Será 0 si no encuentra ese valor, y sino sigue sumando
    return d 

#Agenda que le pases persona y telefono
#Diccionario con clave persona y como valor un forzeset con el valor del numero como String. Hago forze set para no tener repetidos



def añadir (agenda,n,t):
    agenda[n] = agenda.get(n,set()) | {t} #Union si está y si no 
    
def eliminar (agenda,n,t):
    agenda[n] = agenda.get(n,set()) - {t} #Diferencia si está y si no es como un conjunto vacio
    #agenda[n] = agenda.get(n,set()).remove(t)

#Hacer el está 
 
agenda = {}
añadir (agenda, "juan" , "123")
añadir (agenda, "pepe" , "123")
añadir (agenda, "carl" , "123")
eliminar (agenda, "juan", "123")

print(esta(agenda,"pepe" , "123"))
print(esta(agenda,"carl" , "123"))       

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
