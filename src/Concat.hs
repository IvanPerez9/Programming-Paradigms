
module Concat where

import Data.Char;

-- 2. Utilizar listas por comprension, y haga la funcion concat. 
-- Implementar concat reciba una lista de listas y lo devuelva en una sola

concatF :: [[Int]] -> [Int]
concatF lista = [x|sublista <- lista, x <- sublista]


-- Dos generadores, 1 para recorrer la lista grande y otro para la pequeña
-- El generador de la derecha es el que más rapido va