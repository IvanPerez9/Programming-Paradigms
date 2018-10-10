module DefinicionTipos.AlturaArbol where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

alturaArbol :: Arbol a -> Int
alturaArbol AV = 0 
alturaArbol (Nodo raiz AV AV) = 1
alturaArbol (Nodo raiz izq der) = 1 + maximo(alturaArbol(izq),alturaArbol(der))

maximo :: (Int,Int) -> Int
maximo (x,y) = if (x>y) then x else y