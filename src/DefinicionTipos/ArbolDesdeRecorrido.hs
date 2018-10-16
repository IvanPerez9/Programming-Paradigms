module DefinicionTipos.ArbolDesdeRecorrido where

data Arbol a = AV | Nodo a (Arbol a) (Arbol a) deriving Show

a1 = Nodo 1(Nodo 7(Nodo 2 AV AV)AV) (Nodo 4(Nodo 6 AV AV)(Nodo 5 AV AV))

-- Dado un recorrido preorden e inorden sacar un arbol
-- Necesitas lo de comparacion para comparar arboles genericos -> Contexto

reconstruir ::(Eq a) =>  [a]->[a] -> Arbol a
reconstruir [] [] = AV
-- preorden del izque y inorden. Preorden de derecho y inorden
reconstruir (p:ps) inorden = Nodo p (reconstruir pri ini)(reconstruir prd ind)
							where 
							(ini,ind) = partirI inorden p [] -- PartirInorder por la raiz y el acumulador
							(pri,prd) = partirD ps (length ini)[] -- Partir la lista en base a la longitud
							
							
partirI :: (Eq a) =>  [a]-> a ->[a]-> ([a],[a])
partirI (x:xs) p acum = if x == p then (acum,xs) else partirI xs p (acum ++ [x])

partirD :: [a]->Int->[a]-> ([a],[a])
partirD (x:xs) elementos acum = if elementos == 0 then (acum,xs) else partirD xs (elementos -1) (acum++[x])