module DefinicionTipos.NumHojasArbol where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

numHojas :: Arbol a -> Int
numHojas AV = 0
numHojas (Nodo raiz AV AV) = 1
numHojas (Nodo raiz izq der) = numHojas izq + numHojas der