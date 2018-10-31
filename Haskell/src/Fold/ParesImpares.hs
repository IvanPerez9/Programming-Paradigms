module Fold.ParesImpares where


-- Funcion que devuelva una dupla con los elementos impares a un lado y los pares al otro

paresImpares :: [Int] -> ([Int],[Int])
paresImpares lista = foldr (\x (a1,a2) -> if (x `mod` 2 == 0) then (a1, a2++[x]) else (x:a1 , a2)) ([],[]) lista

-- Lo de los : y ++ es lo mismo pero el ++ solo vale en un orden


