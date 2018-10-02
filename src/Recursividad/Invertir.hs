module Recursividad.Invertir where


invertir :: [Int] -> [Int]
invertir l = foldl(\ acum x->x:acum)[] l

-- No necesita de caso base, porque ya lo incorporamso con el propio acumulador de foldl