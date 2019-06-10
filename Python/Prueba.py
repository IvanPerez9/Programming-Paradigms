"""
CUBINFINITO
Un número es cubifinito si al elevar al cubo sus dígitos y
sumarlos da como resultado 1 u otro número cubifinito. Crear
una función que reciba un número y devuelva si es cubifinito
"""
def digitos2(num):
    l = []
    for e in str(num):
        l.append(e)
    return l


def cubifinito(numero):
    suma = sum([int(x) ** 3 for x in str(numero)])
    anterior = 0
    respuesta = str(numero)
    while suma != 1 and anterior != suma:
        anterior = suma
        suma = sum([int(x) ** 3 for x in str(suma)])
        respuesta += ' -> ' + str(suma)
    if suma == 1:
        respuesta += ' -> cubifinito.'
    else:
        respuesta += ' -> ' + str(suma) + ' -> no cubifinito.'
    return respuesta

def cubifinito2(num):
    resultado = sum([int(x)**3 for x in str(num)])
    if resultado == 1:
        return True
    elif sum([int(x)**3 for x in str(resultado)]) == 1:
        return True
    else:
        return False
    return resultado == 1 or cubifinito(resultado) == 1

def cubifinito3 (num):
    suma = 0
    for e in str(num):
        suma += int(e ** 3)
    if suma == 1 :
        print("Cubifinito")
    elif suma > 10:
        return cubifinito3(suma)
    else:
        print("No es cubifinito")


print(cubifinito(100))
print(cubifinito2(1243))
print(cubifinito3(1243))

def addTo(e, t):
    for s in t:
        s += [e]
    return t


def conjunto_potencia(a_set):
    if not a_set: return [[]]
    e = a_set[0]
    t = a_set[1:]  # Todos menos el primero
    return conjunto_potencia(t) + addTo(e, conjunto_potencia(t))

print("Conjunto potencia: ")
print(conjunto_potencia([1, 2, 3, 4, 5]))
