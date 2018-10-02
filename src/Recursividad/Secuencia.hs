module Recursividad.Secuencia where


-- Numero de secuencia de 0 que hay [0,1,0,0,3,4,1,0,0,3,4,0,0,234,0,9,0] -> 6
-- Truco contar la secuencia cuando ya la has acabado

-- Como la cuento ???? 

secuencia :: [Int] -> Int
secuencia [] = 0
secuencia [0] = 1
secuencia [x] = 0
secuencia (0:0:xs) = secuencia(0:xs)
secuencia (0:x:xs) = 1 + secuencia xs
secuencia (y:x:xs) = secuencia (x:xs)

