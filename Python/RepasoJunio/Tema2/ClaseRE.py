import re

# Que cadena evalua ab* -> Una a seguida de 0 o N b

r1 = re.match("ab*" , "a")

# Que patron evalua la cadena "ababab...ab" -> Necesario el $ para que finalice en ab

r2 = re.match("(ab)*$" , "ababababab")

# Dado el patron "a.*c" y la cadena "abcabc, Que evalua -> A seguido de cualquier cosa 0 o N veces, y terminado en c
# Sin el $ si encuentra otra A es como si siguiese, no solo se para en C
r3 = re.match("a.*c" , "agcabcgd")

# Que patron evalua una A seguida de 3 o más B

r4 = re.match("a(b){3,}" , "abb")

# Que patron evalua la primera palaba de una cadena
# Sin el + es la primera letra
r5 = re.match("[^ ]+" , "Hola que tal")

#Evaluar si las casillas de ajedrez están bien -> Ir de minusculas a mayusculas y
# ? es voraz, busca la menor cadena posible ???

r6 = re.match("[a-hA-H][0-9]+" , "H3a2")

# Funcion que diga si es valido el identificador para una variable

r7 = re.match("[_]*[a-z]+[_0-9a-zA-Z]*" , "Vvariable")

# Subcadena contenida en un String
# Modo no voraz, obtener la primera
r8 = re.match("(abc)+?" , "abcabcabs")
r82 = re.search("abc" , "abcsdab")
print(r8)
print(r82)

#Recibir una cadena y devolverla sin espacios en blanco

r9 = re.sub(" " , "" , "Hola que tal")

# Devolver cuantas veces aparece la palabra "esta" -> Poner \b para delimitar la palabra, para usar esto tenemos que poner r

r10 = re.findall(r"\besta\b" , "esta estanteria esta atestada")
print(len(r10))

# Crear funcion que devuelva numeros [1,2,23] con [001,002,023]

def funcion (lista):
    listaAux = list()
    n = len(str(max(lista)))
    for i in lista:
        listaAux.append(str(i).zfill(n +1))
    return listaAux

print(funcion([1,2,23]))

# Crear funcion para ver si una cadena es capicua

def capicua (cadena):
    contador = 0
    indice = -1
    for i in range(0 , len(cadena)):
        if cadena[i] == cadena[indice]:
            contador += 1
            indice -= 1
    if len(cadena) == contador :
        print("Es capicua")
    else:
        print("No es capicua")

capicua("hoha")