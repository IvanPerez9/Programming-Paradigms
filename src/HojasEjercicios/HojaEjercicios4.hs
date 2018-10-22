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


-- Se pide definir una función que calcule el espejo de un árbol. 

data ArbolD a = AVD | RamaD (ArbolD a) a (ArbolD a) deriving Show
ejercicioD :: (Show a) => ArbolD a -> ArbolD a
ejercicioD AVD = AVD
ejercicioD (RamaD AVD r AVD) = (RamaD AVD r AVD)
ejercicioD (RamaD izq r der) = RamaD (ejercicioD der) r (ejercicioD izq) -- Ojo los parentesis 

{- Ejercicio I 
Se pide crear una nueva CLASE de tipos, llamada Coleccion, para representar
colecciones de datos de cualquier tipo, donde los tipos pertenecientes a
esta clase tendrán el siguiente comportamiento:

	esVacia: función para saber si la colección está vacía.
	insertar: insertará un nuevo elemento en la colección.
	primero: devolverá el primer elemento de la colección.
	eliminar: eliminará un elemento de la colección.
	size: devolverá el número de elementos de la colección.
	
Algunas de las funciones anteriores variarán su implementación en función
del tipo de colección particular que sea instancia de la clase Coleccion. Por
ello, se pide crear dos instancias diferentes de esta clase para los dos
nuevos tipos de datos que se presentan a continuación:
data Pila a = Pil [a] deriving Show
data Cola a = Col [a] deriving Show
-}

data Pila a = Pil [a] deriving Show
data Cola a = Col [a] deriving Show

-- Poner la "Collecion" "c" y luego "El tipo de Dato" "a" 

class Collection c where 
				 esVacia :: c a -> Bool
				 insertar :: c a -> a -> c a
				 primero :: c a -> a
				 eliminar :: c a -> c a
				 size :: c a -> Int

-- Siempre que se toque la pila/cola o lo que sea, poner el constructor
instance Collection Pila where
				 esVacia (Pil a) = length a == 0
				 insertar (Pil a) b = Pil (a ++ [b]) -- Se inserta por el final
				 primero (Pil a) = last a
				 eliminar (Pil a) = Pil (init a)
				 size (Pil a) = length a


