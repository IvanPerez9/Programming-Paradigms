# Teoria Python

__1. Tema 2__

* __1.1__ Objetos.

    - Se puede usar objetos con las clases.
        - Funciones dentro de clases -> Metodos de clases.
        - Todos reciben "Self" como primer parametro.
        - Los atributos de clase se instancian cuando se usan
    - Es obligatoria la documentacion
    - El constructor de la clase es con: ` __init()___`
    - Debemos inicializar todas la variables en el constructor, se usen o no.
        - Se puede llamar a una funcion de fuera de la clase, llamandola a traves de una variable, como si fuera un atributo
   
* __1.2__ Entrada Salida.

    - Para leer/escribir convencionalmente de entrada salida hemos usado -> input y print
    - Para leer/escribir ficheros -> Mejor sintaxis con "with"
    
        ``` 
        with open ("data.txt" , "r" ) as f:
                for line in f:
                    print(line)
        ```
     
     - Con esta sintaxis no hace falta cerrar el fichero.
     

* __1.3__ Herencia.

    - Permite tener clases heredadas, poniendolas entre parentesis en otras clases
    
        ```
        class Perro(Mamifero, Domesticado):
        ```
     - Para tener partes privadas, ya sea metodo o atributo poner __
        - Llamar al metodo de la clase base con super( )
        - Apoyarnos en las variables privadas, junto con publicas para sobreescribir metodos sin romper llamadas internas

* __1.4__ Excepciones.

    - Capturar con un bloque de try .. except
    - Pueden tener varios bloques `Except Error` o capturar varios en el mismo except
    - La unica forma de saber cual es el error a capturar es hacerlo mal primero

* __1.5__ Modulos.

    - Módulo .math para randoms y operaciones aritmeticas
    - Módulo .statistisc para operaciones estadísticas como la moda y la media
    - Módulo .decimal para la precision si hay que redondear numeros
    - Módulo .date y .datetime para dar formato a fechas y horas
        - Se puede dar formato a la informacion de la hora con strftime( )
    - Módulo .sys se usa para hacer que librerias cargen antes o despues de nuestro propio codigo
        - Se ve mucho con ` if __name__ == '__main__': ` 
        - Todo tiene que ver con el interprete de Python, y todo modulo tiene un atributo llamado __name__ que define el espacio de nombres en el que se está definiendo.
        - El nombre " __main__ " es donde está tú codigo, 
            - El intérprete pasa el valor del atributo a '__main__' si el módulo se está ejecutando como programa principal
            - Si es importado desde otro módulo, el atributo __name__ pasa a contener el nombre del archivo en si
     - Módulos de colecciones que extienden.
        - namedTuple : Tuplas cuyos campos tienen un nombre, se usan para obtener estructuras tipo C
        - Deque: Insercion y eliminacion eficientes por cualquier extremo. Más eficientes que las listas como colas.
            - El insert no es eficiente, porque deplaza toda la lista
        - OrderectDict: Diccionario con un orden de insercion
        - Counter: Diccionario que lleva la cuenta de los objetos hasheables. Es expecifico para contar claves.
        
     - Modulo numpy -> `import numpy as np `
        - Modulo de arrays, limitado a tipos primitivos.
        - Array multidimensional homogeneo
        - np.array ([1,2,3]) es más eficiente para iterar que las listas
        - Acceso con [1] 
        - Tienen metodo `arrange()` que funciona como los Slyce (Start,Stops,Step)
     - Módulos de expresiones regulares:
        - Dot (.) : Cualquier caracter excepto el salto de line \n
        - Caret (^) : Inicio de String o inicio de linea. No tiene sentido con match
        - Dollar ($) : Final de String, sirve para asegurarse que no queda nada
        - (*) : La RE previa 0 o N veces
        - (+) : La RE previa 1 o N veces
        - (?) : La RE previa 0 o 1 vez. Modo no voraz
        - {m} : La RE previa m veces
        - {n,m} : La RE previa entre n y m veces
        - [_] : Cualquier caracter del set
        - [^] : Cualquier caracter que no sea del set
        
        - Se puede agrupar varias RE entre ( ) y luego hacerlas referencia con \nº
        - Funciones RE (re.)
            - match: Hace match a lo que buscamos
            - search: Busca el primero en cumplir el patron
            - findall: Busca todos los que cumple el patron
            - sub: Substituye el substring por otro
            - compile: Permite procesar el patron
