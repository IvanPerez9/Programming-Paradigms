# Teoria Python

__1. Tema 1__

* __1.1__ Compiladores e Interpretes.

    - Traduccion lenguaje de alto nivel a codigo maquina.
    - El compilador lee completamente un programa y lo traduce entero. No lo repite.
    - Interprete lee instruccion a instruccion, traduce y ejecuta.
      - Se repite con cada ejecucion
      - No hay proceso separado de ejecucion, traduccion.
    - Python es interpretado, multiplataforma, multifuncional, multiparadigma.
    
* __1.2__ Tipado.

    - Toda variable tiene un tipo
    - Realizar conversion si no son del mismo tipo.
    - Una misma variable puede tomar valores de distinto tipo.
    - El tipo de la variable se determina en tiempo de ejecucion.

* __1.3__ Lenguaje Pyhton

    - Division (/) Division entera (//) Resto (%)
    - 3 tipos de numericos -> Int , float y complex
    - Conversion implicita
    * __1.3.1__ Bucles y Sentencias:
    
        - El for no itera hasta una condicion, usar o lista de elementos o range()
        - Strings tanto con comillas dobles como simples
        - Concatenar con + . Se puede usar simbolos aritmeticos con strings
        - Range () puede tener 1,2 o 3 parametros
        - Bucle While tiene una condicion : Se puede salir con un "break" o forzar iteracion con "continue"
        
 * __1.4__ Funciones
    
     - No se especifica el valor de retorno
     - Siendo "DINAMICO" no se especifica el valor de los parametros de entrada, el tipo estará contenido en la llamada
     - Fuertemente tipado
     - Se completa la funcionalidad con bibliotecas como math
     - Se le puede pasar valores por defecto a una funcion
     
     - Tuplas: Son coleeciones Heterogeneas, ordenadas e inmutables
        - Acceso a los elementos [ ]
        - Se pueden desempaquetar, coger solo 1 parte de la tupla
        - funciones como len() para iterar dentro de la tupla
     
     - Listas: Colecciones heterogeneas, ordenadas y mutables
        - Acceso a elementos [ ]
        - Añadir elementos con append()
        - Iterar por ella con for()
        - Copiar listas -> lista1 = lista2 [:]
        - Se puede insertar en una posicion en concreto. l2.insert(0,e)
        
     - Slice: Acceso a Elementos
        - Acceder al final [-1]
        - Se puede acceder a rangos, entre 0 y 2 -> [0:2]
        - Últimos 2 items del array -> a[-2:]
        - Selecciona todos los elementos excepto los dos últimos -> a[:-2]  
        - a[inicio:final:salto]
        
     - Set(Conjuntos) : Coleccion desordenada, mutable de objetos hasheables
        - Usar { } o mejor el constructor set()
        - soporta len() y acceso con "in"
        - Para insertar usa add()
        - Funciones de union " | " , interseccion " & "  , diferencia " - "
      
     - FrozenSet : Son inmutables, y por lo tanto hasheables
         - Constructor es forzenset()
         - tiene funciones de union(), interseccion(), issubset() , issuperset()
         - La copiar con s2 = s1.copy()
         
     - Diccionario: Coleccion de parejas clave, valor. Clave hasheable y valor arbitrario
          - Con { } o con dict()
          - Separar clave,valor con " : " ` d2 = dict({“one” : 1, “two” : 2, “three” : 3}) `
          - Se puede iterar por las parejas con un for ->
          ` for k,v in diccionario: ` 
          - Se puede construir con una lista de tuplas.
          
            ` d = dict([(“one”: 1), (“three”: 3), (“two”: 2)]) `

          -  `d.keys() # lista de claves`
          
             `d.values() # lista de valores`
             
             `d.items() # lista de clave valor`
             
          - Acceso a la clave directamente d[ i ] . Incluso modificar  el valor de esa clave con d[ i ] = 8 
          - Para acceder al valor asociado a una determinada clave, se lo hace de la misma forma que con las listas, pero utilizando la             clave elegida en lugar del índice.

            `print materias["lunes"]`
         
          - Sin embargo, esto falla si se provee una clave que no está en el diccionario. Es posible, por otro lado, utilizar la función             get, que devuelve el valor None si la clave no está en el diccionario, o un valor por omisión 
            que se establece opcionalmente.

          - Para verificar si una clave se encuentra en el diccionario, es posible utilizar la función has_key o la palabra reservada in
   
