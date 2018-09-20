module Divisores where

import Data.Char;

-- Divisores de un numero. Factores de 24 {1,2,3,4,6,8,12,24}

factores :: Int -> [Int]
factores n = [x|x <-[1..n], n`mod`x ==0]

-- Si es mod 0, es divisor se guarda en una lista. Uso un generador recorrer los posibles divisores
-- mod y rem son lo mismo 