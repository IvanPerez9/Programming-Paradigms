module Recursividad.Pertenece where


-- Funcion que busque en un lista un entero

--pertenece2 :: ([Int], Int) -> Bool
--pertenece2 ([] , e) = false
--pertenece2 (x:xs , e) = if x == e then true
--pertenece2(x:xs ,e) = pertenece (

pertenece :: Int -> [Int] -> Bool
pertenece_[] = False
pertenece x(y:ys) = (x==y) || (pertenece x ys)

-- Son como mis dos recursivos a la vez 


-- Lista dos elementos, el primero lo sustituyes por el sugundo 
-- Todas las apariciones del primer elemento las sustituyes por el segundo 

cambio ::Int->Int->[Int] -> [Int]
cambio _ _ [] = []
cambio x y (z:zs) = if (z == x) then y:(cambio x y zs) else z:(cambio x y zs)   
-- cambio 1 2 [1,1,1,1]
