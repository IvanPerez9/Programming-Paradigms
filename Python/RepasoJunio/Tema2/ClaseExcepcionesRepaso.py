
def avisarNoEntero ():
    try:
       n = int(input("Introduce un entero: "))
       print(n)
    except ValueError:
        print("No es un entero")

# Fallar si carga un fichero
def cargaFicheroEX ():
    try:
        with open("FicheroRepasoHeroeee" , "r") as f:
            print(f.readline())
    except FileNotFoundError:
        print("No existe ese archivo")

#Funcion get del diccionario -> Dic, clave, elemento. Devolver valor asociado a la clave o elemento si no esta
def diccionarioKV (diccionario , clave , e):
    try:
        print(diccionario[clave])
    except KeyError:
        print("No existe esa clave: " + e )

if __name__ == '__main__':
    #avisarNoEntero()
    #cargaFicheroEX()
    dic = {"Uno" : 1, "Dos" : 2 , "Tres" : 3}
    diccionarioKV(dic, "Unno" , "ElementoSalida")