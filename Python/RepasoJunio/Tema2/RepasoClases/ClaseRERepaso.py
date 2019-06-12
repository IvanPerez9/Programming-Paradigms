import re

# Que cadena evalua ab* -> Una a seguida de 0 o N b

r1 = re.match("ab*" , "abbb")
print(r1)

# Que patron evalua la cadena "ababab...ab" -> Necesario el $ para que finalice en ab

r2 = re.match("(ab)+" , "ababababababab")
print(r2)

# Dado el patron "a.*c" y la cadena "abcabc, Que evalua -> A seguido de cualquier cosa 0 o N veces, y terminado en c
# Sin el $ si encuentra otra A es como si siguiese, no solo se para en C

r3 = re.match("a.*c" , "agfdjigodngioc")
print(r3)

# Que patron evalua una A seguida de 3 o más B

r4 = re.match("a(b){3,}" , "abbb")
print(r4)

# Que patron evalua la primera palaba de una cadena
# Sin el + es la primera letra

r5 = re.match("[^ ]+" , "hola que")
print(r5)

#Evaluar si las casillas de ajedrez están bien -> Ir de minusculas a mayusculas y
# ? es voraz, busca la menor cadena posible ???

r6 = re.match("[a-hA-H][0-8]+" , "H8")
print(r6)

# Funcion que diga si es valido el identificador para una variable

r7 = re.match("[_]*[0-9a-z]+[a-zA-z0-9]*" , "vVariable")
print(r7)

# Subcadena contenida en un String
# Modo no voraz, obtener la primera

r8 = re.match("(ab)+?" , "dabacd") # No es totalmente igual
r82 = re.search("ab" , "adabacd")
print(r8)
print(r82)

#Recibir una cadena y devolverla sin espacios en blanco

r9 = re.sub(" " , "" , "hola que tal")
print(r9)

# Devolver cuantas veces aparece la palabra "esta" -> Poner \b para delimitar la palabra, para usar esto tenemos que poner r

r10 = re.findall(r"\besta\b" , "esta palabra esta delimitada")
print(len(r10))

# Crear funcion que devuelva numeros [1,2,23] con [001,002,023]

def funcion1 (lista):
    aux = list()
    n = len(str(max(lista)))
    for i in lista:
        aux.append(str(i).zfill(n))
    return aux

print(funcion1([1,2,33, 444]))

# Crear funcion para ver si una cadena es capicua

def funcion2 (cadena):
    indice = -1
    contador = 0
    for i in range(0, len(cadena)): # Si no saca nada ojo con el range
        if cadena[i] == cadena[indice]:
            contador += 1
            indice -= 1
    if contador == len(cadena) :
        print("Es capicua")
    else:
        print("No es capicua")

funcion2("oco")