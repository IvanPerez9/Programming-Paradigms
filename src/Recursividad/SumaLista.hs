module Recursividad.SumaLista where

import Data.Char

suma :: [Int] -> Int
suma [] = 0
suma lista = head lista + suma (tail lista)

-- suma (x:xs) = x + suma xs 
-- Son iguales x es el primer elemento y el resto xs 

suma2 :: [Int] -> Int
suma2 lista = suma2'(lista,0)

-- Con parametro de acumulacion

suma2' :: ([Int], Int) -> Int
suma2' ([], acum) = acum
suma2' (x:xs, acum) = suma2' (xs,acum+x)


-- Invertir los elemento de una lista con recursividad no final

invertir :: [Char] -> [Char]
invertir [] = []
invertir (c:cs) = invertir cs ++ [c]

-- c es la lista y lo otro el resto de elementos 