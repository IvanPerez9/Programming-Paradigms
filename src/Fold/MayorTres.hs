module Fold.MayorTres where


-- n Mayor 3 [1,3,4,5,7] la lista con los 3 mayores -- Con recursividad normal 

mayorTres :: [Int] -> [(Int,Int,Int)]
mayorTres lista = foldl (\(y,z,t) x -> if (x > y) then (x,z,t) else if x>z then (y,x,t) else if x>t then (y,z,x) else (y,z,t):mayorTres x ) [()] lista