module Genericos.CambioMinMax where

import Data.Char
-- Cambiar minusculas por mayusculas y al reves
-- map es una funcion que aplica una condicion a cada elemento de la lista 

minMax :: [String] -> [String]
minMax lista = map (foldl(\acum c -> if isUpper c then acum++[toLower c] else acum++[toUpper c])[]) lista
-- No se puede hacer aqui un acum:c ????

-- Foldl sin el tercer argumento porque se lo pasa el map 

