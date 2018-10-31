module DefinicionTipos.InsertarArbol where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

-- En un arbol binario de busqueda
-- Necesito comparar para poder saber por donde voy a insertar

-- Ord para que solo le pase tipos con los que se pueda operar = < >

insertarArbol::(Ord a) => Arbol a -> a -> Arbol a
insertarArbol AV n = (Nodo n AV AV)
insertarArbol (Nodo r izq der) valor = if valor>r then (Nodo r izq (insertarArbol der valor)) 
									   else (Nodo r (insertarArbol izq valor) der)