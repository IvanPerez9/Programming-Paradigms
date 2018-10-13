module DefinicionTipos.ArbolDesdeRecorrido where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

-- Dado un recorrido preorden e inorden sacar un arbol

arbolDesdeRecorrido :: Arbol preorden -> Arbol inorden -> Arbol final
arbolDesdeRecorrido AV AV = AV