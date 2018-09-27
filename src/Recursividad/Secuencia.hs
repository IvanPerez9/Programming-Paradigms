module Recursividad.Secuencia where


-- Numero de secuencia de 0 que hay [0,1,0,0,3,4,1,0,0,3,4,0,0,234,0,9,0] -> 6
-- Truco contar la secuencia cuando ya la has acabado

secuencia :: [Int] -> Int
secuencia [] = 0


-- Otro: MergeSort 
