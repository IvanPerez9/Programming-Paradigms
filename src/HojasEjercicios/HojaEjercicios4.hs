module HojasEjercicios.HojaEjercicios4 where

{-
Listado de ejercicios para poner en práctica los conocimientos adquiridos sobre definición de tipos
sinónimos y nuevos tipos, tipos recursivos y tipos recursivos polimórficos. Y también sobre el
manejo de clases de tipos en Haskell.
-}

--  Se quiere ordenar los elementos de una lista (cuyos elementos son comparables) mediante el algoritmo del quicksort.

ejercicioA :: Ord a => [a] -> [a]
ejercicioA [] = []
ejercicioA (x:xs) = ejercicioA [z | z <- xs, z<x] ++ [x] ++ ejercicioA [y | y <- xs, y>=x]

{-
Ejercicio B
Se pide implementar una funcion que dado un numero (de cualquier tipo que
soporte la operacion de division) y una lista de numeros del mismo tipo,
divida a ese numero por cada uno de los elementos contenidos en la lista y
devuelva una lista con el resultado.
-}

ejercicioB :: Float ->  [Float] -> [Float]
ejercicioB _ [] = []
ejercicioB num lista = foldl (\acum x -> [num/x] ++ acum) [] lista

{-

Dado un nuevo tipo de datos para representar un árbol binario de cualquier tipo, definido
como sigue:
data Arbol a = AV | Rama (Arbol a) a (Arbol a)
Se pide definir una función que visualice el árbol por pantalla de una determinada forma:
separando cada hijo izquierdo y derecho por “|”, la raíz entre guiones y cada nivel diferente
del árbol por “( )”.

 mostrarArbol (Rama AV 5 (Rama AV 4 AV))
"()|-5-|(4)"


-}

data Arbol a = AV | Rama (Arbol a) a (Arbol a)

ejercicioC :: (Show a) => Arbol a -> String
ejercicioC AV = ""
ejercicioC (Rama AV r AV) = "|-" ++ show r ++ "-|" 
-- Rama es el constructor de tipo 
ejercicioC (Rama der r izq) = "(" ++ ejercicioC (der) ++ ") |- " ++ show r ++ " |- (" ++ ejercicioC (izq) ++ ")" 

