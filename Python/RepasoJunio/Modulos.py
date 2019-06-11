import collections

# NAMETUPLE

elemento = collections.namedtuple("elemento" , ["Nombre" , "simbolo" , "num"])
e = elemento("Azufre" , "S" , "14")

print(e)
print(e.Nombre)

# DEQUE -> Insercion y eliminacion eficiente por cualquier extremo

lista = ["uno" , "dos" , "tres"]
deq = collections.deque(lista)

print(deq) #len()
print(deq[0])

deq.remove("dos")
print(deq)
deq.append("doos") #Inser para añadir en la posicion deseada
print(deq)
deq.appendleft("prueba") # Añadir el primero
print(deq)
deq.extend("hola")
print(deq)
deq.extendleft(["hola", "que"])
print(deq)
deq.rotate(-1) #Cambia la posicion a la primera del elemento pasado
print(deq)

#COUNTER

# elementos:
lista1 = ['Granada', 'Huelva', 'Sevilla', 'Granada',
          'Granada', 'Sevilla', 'Sevilla']

# Crear un objeto Counter a partir de la lista lista1
cuenta1 = collections.Counter(lista1)

# En el objeto Counter las claves son los
# elementos (sin repetir) de la lista y los valores el
# número de veces que aparece cada elemento en la lista.
print(cuenta1)

#Contador nuevo y luego update -> acceso con []

con = collections.Counter()
con.update("xxxxyyzzzzzt")
print(con)

#Sacar una lista y ordenarla
listaCon = list(con.elements())
print(listaCon)
listaCon.sort()
print(listaCon)

#Obtener el elemento mas comun o los dos mas comunes
print(con.most_common(1))
print(con.most_common(2))

#Como cualquier diccionario recorrido K y V -> ojo concatenado con ","

for clave, valor in con.items():
    print(clave, ":" , valor)
