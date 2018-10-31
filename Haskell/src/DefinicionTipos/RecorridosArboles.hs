module DefinicionTipos.RecorridosArboles where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

inOrder :: Arbol a -> [a]
inOrder AV = []
inOrder (Nodo r izq der) = inOrder izq ++ [r] ++ inOrder der

preOrder :: Arbol a -> [a]
preOrder AV = []
preOrder (Nodo r izq der) = [r] ++ preOrder izq ++ preOrder der

postOrden :: Arbol a -> [a]
postOrden AV = []
postOrden (Nodo r izq der) = postOrden izq ++ postOrden der ++ [r]