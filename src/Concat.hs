
module Concat where

import Data.Char;

-- 2. Utilizar listas por comprension, y haga la funcion concat. 
-- Implementar concat reciba una lista de listas y lo devuelva en una sola

concatF :: [a] -> [a] -> [a]
concatF [][] = []
