module SumaCuatro where

import Data.Char;

-- Ejercicio j de la parte 2 
-- Implementar una funcion que devuelva True si la suma de los cuatro primero elementso de una lista de numeros
-- Enteros es un valor menor a 10 y false si el caso contrario. Ajuste de patrones

sumaCuatro :: [Int]-> Bool
--sumaCuatro (x:y:w:z:zs) =if (x+y+w+z)<10 then True else False

sumaCuatro (x:y:w:z:zs) = (x+y+w+z) <10
sumaCuatro_ = False

 --[if x >10 then True else False |x <- n]

-- Es una lista de minimo 4 elementos 