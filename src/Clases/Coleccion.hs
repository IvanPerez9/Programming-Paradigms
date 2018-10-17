module Clases.Coleccion where

import Data.Char

-- Ejercicio i de la hoja 4

{- 
Se pide crear una nueva clase de tipos, llamada Coleccion, para representar
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

-- Poner la "Collecion" y luego "El tipo de Dato" 

class Coleccion c where 
				  esVacia :: c a -> Bool
				  insertar :: c a -> a -> c a
				  primero :: c a -> a 
				  eliminar :: c a -> c a 
				  size :: c a -> Int 
				  
-- Si toco la collecion, ya sea una pila o cola, definir su constructor de tipo

instance Coleccion Pila where
						esVacia (Pil a) = length a == 0 
						insertar (Pil a) z = Pil (a++[z])
						primero (Pil a) = last a
						eliminar (Pil a) = Pil (init a)
						size (Pil a) = length a
		
instance Coleccion Cola where
						esVacia (Col a) = length a == 0
						insertar (Col a) b = Col (a++[b])
						primero (Col a) = head a
						eliminar (Col a) = Col (tail a)
						size (Col a) = length a
						
						
-- Ojo con la diferencia entre Last vs Tail  && Init vs Head

-- Last: Devuelve solo el ultimo elemento
-- Tail: Devuelve toda la lista menos el primer elemento

-- Init: Devuelve todo menos el primer elemento
-- Head: Devuelve el primer elemento