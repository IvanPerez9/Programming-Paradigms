module DefinicionTipos.NumNodosArbol where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))


numNodos :: Arbol a -> Int
numNodos AV = 0
numNodos (Nodo raiz izq der) = 1 + numNodos izq + numNodos der