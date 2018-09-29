module Recursividad.Secuencia where


-- Numero de secuencia de 0 que hay [0,1,0,0,3,4,1,0,0,3,4,0,0,234,0,9,0] -> 6
-- Truco contar la secuencia cuando ya la has acabado

-- Como la cuento ???? 

secuencia :: [Int] -> Int
secuencia [] = 0
secuencia x:xs = if (x==0) then x : (secuencia xs) else secuencia xs++