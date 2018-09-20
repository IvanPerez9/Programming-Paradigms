module Mayusculas where

import Data.Char;

-- Numero de mayusculas que tiene un String
-- Listas por comprension, eliminar los que no sean mayusculas

nMayusculas :: String -> Int
nMayusculas s = length [c|c <- s, isUpper c] 


-- 2 ejercicios, 1 sencillo:
-- 1. Que cambie las mayusculas por minusculas y las mayusculas por minusculas
-- 2. Utilizar listas por comprension, y haga la funcion concat. Implementar concat reciba una lista de listas y lo devuelva en una sola