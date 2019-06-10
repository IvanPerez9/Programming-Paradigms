import random
# Crear dada una altura una piramide

n = int(input("Altura piramide: " ))

for i in range(n):
	espacios = n -i
	print(" " * espacios + "*" * (i*2+1))

# Piramide invertida

for i in range((n-1) , -1 , -1):
	espacios = n-i
	print(" " * espacios + "*" * (i*2+1))

# Factorial de un numero

def factorial (num):
	if num == 0 :
		return 1
	else:
		return num * factorial(num-1)

# Funcion que devuelva la lista de numeros primos del 0 al 100

def isPrime (num):
	if num < 0 :
		return False
	elif n == 2:
		return True
	else:
		for i in range(2,num):
			if (num%i) == 0 : # si es divisible por algo que no es él
				return False
		return True

def listaPrimos ():
    l = list()
    for i in range(2,100):
        if isPrime(i):
            l.append(i)
    return l

# Crear un funcion que recibe un numero y devuelve una lista con sus digitos

def digitos (num):
	l = list()
	for i in str(num):
		l.append(i)
	return l

def digitos2 (num):
	l = list()
	while num :
		l.append(num % 10)
		num = num // 10
	return l

# numeros perfectos -> Si la suma de sus divisores es igual a si mismo como el 28

def divisores (num):
	lista = list()
	for i in range(num):
		if (num % i ) == 0:
			lista.append(i)
	return lista

def perfectNum (num):
	suma = 0
	l = divisores(num)
	for i in range(len(l)):
		suma += l[i]
	if suma == num :
		print("Es perfecto")
	else:
		print("No es perfecto")

# Recibir lista de numeros y devuelve lista de tuplas por cada numero. Con num, cuadrado y cubo

def tuplasNumero (lista):
	listaSalida = list()
	for i in range(len(lista)):
		tupla = (i , i**2 , i*i*i)
		listaSalida.append(tupla)
	print(listaSalida)

# maximo y minimo de una lista de numeros

def maximo (lista):
	print(max(lista))

# Invertir una cadena

def invertir (cadena):
	print(cadena[::-1])

# Cadena pero con la primera letra en mayus

def mayusCadena (cadena):
	print(cadena[0:1].upper() + cadena[1::].lower())

# imprimir una matriz -> lista de listas

def imprimirMatriz (m):
	for i in range(len(m)+1):
		for e in range(len(m)):
			print(m[e][i], end= "")

#funciones de pila y cola -> apilar, desapilar ... etc

def apilar (pila, e):
	pila.append(e)
	return pila

def desapilar (pila):
	pila.pop()

def cima (pila):
	return pila[-1]

def encolar (cola, e):
	cola.insert(0,e)
	return cola

def desencolar (cola):
	cola.pop()

def primero (cola):
	cola[-1]

#Parentesis balanceados o no

def balanceados (cadena):
	pila = []
	pila2 = []
	for i in cadena:
		if i == "(" :
			apilar(pila,i)
		elif i == ")" :
			apilar (pila2, i)
	if len(pila) == len(pila2) :
		print("Están balanceados")
	else:
		print("No están balanceados")

def balanceados2 (cadena): # Solo si en orden ? si no nada
	pila = []
	for i in cadena :
		if i == "(":
			apilar(pila,i)
		elif i == ")"  and len(pila) != 0:
			if len(pila) != 0:
				desapilar(pila)
			else:
				print("No está balanceado")
	if len(pila) == 0 :
		print("Balanceados")
	else:
		print("No estan balanceados")

# Funciones de union, interseccion y diferencia entre conjuntos

def union (c1,c2):
	c = c1 | c2
	return c

def union2 (c1, c2):
	c = c1.union(c2)
	return c

def inter (c1,c2):
	c = c1 & c2
	return c

def inter2 (c1,c2):
    c = c1.intersection(c2)
    return c

def diff (c1,c2):
	c = c1 - c2
	return c

def diff2 (c1, c2):
	c =c1.difference(c2)
	return c

c = {1,2,3,4,5,6,7,8}
c2 = {1,2,3,4}
l = [1,1,2,2,3]

# Lista de numeros todos estan repetidos menos 1. Devolver ese 1 que no esta

def repetidos (l):
	aux = list()
	for i in l:
		if i not in aux:
			aux.append(i)
		else:
			aux.remove(i)
	return aux

print(repetidos(l))

# Conjunto de numero devolver una tupla 2 conjuntos, uno con los pares otro con los impares

def paresImpares (c):
	pares = set()
	impares = set()
	for i in c:
		if i % 2 == 0:
			pares.add(i)
		else:
			impares.add(i)
	return (pares, impares)

# Devolver numero de apariciones de cada caracter en una cadena

def caracteres (cadena):
	d = dict()
	for i in cadena:
		if i not in d.keys(): # Not in d solo ?
			d[i] = 1
		else:
			d[i] += 1
	return d

# Numero a apariciones palabra en una frase

def palabras (cadena):
	d = dict()
	palabras = cadena.split()
	for i in palabras:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return d

#– Utilizando el modulo random, crear una función que simule N
# tiradas de 2 dados y cuente las veces que aparece un resultado.

def tiradas (n):
	d = {2:0 , 3:0, 4:0, 5:0, 6:0 , 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
	for i in range(n):
		tirada = random.randint(2,12)
		d[tirada] += 1
	return d

"""
d.keys() # lista de claves
d.values() # lista de valores
d.items() # lista de clave valor

d.get(key[, default]) # No existe, default/None
d.pop(key[, default]) # No existe, default/KeyError

"""
# Contar caracteres pero con get -> diccionario

def contarCaracteres(cadena):
	d = dict()
	for i in cadena:
		d[i] = d.get(i,0) + 1
	return d

#inverso del diccionario

def inverso (diccionario):
	d = dict()
	k = diccionario.keys()
	v = diccionario.values()
	d = dict(zip(v,k))
	return d

#
