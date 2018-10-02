module Recursividad.Invertir where


invertir :: [Int] -> [Int]
invertir l = foldl(\ acum x->x:acum)[] l

-- No necesita de caso base, porque ya lo incorporamso con el propio acumulador de foldl

--Reciba una lista de enteros, un valor y elimine todos los elemtos con ese valor 

eliminar:: [Int]->Int -> [Int]
eliminar lista elemento = foldl(\acum x -> if x==elemento then acum else acum ++ [x]) [] lista

-- Dos parametros foldl, 1 acumulador y 2 el elemento x de la lista

