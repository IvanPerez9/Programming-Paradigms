module Fold.Veces where


--Lista de numeros enteros,separar en una dupla de enteros, los elementos que esten una vez y los elementos que esten mas de 1

veces :: [Int] -> ([Int],[Int])
--veces2 lista = foldl(\acum x -> if (pertenece(x,acum)) then ([x],[]) else ([],[x])) ([],[]) lista
-- Acumulador de unicos y repes
veces lista = foldl(\(unicos,repes) x -> if (pertenece(x,repes)) then (unicos,repes)
										 else (pertenece x unicos) then (borrar x unicos, repes ++[x])
										 else (unicos ++ [x],repes) ([],[]) lista


-- Subfuncion de estar en una lista
esta :: [Int] -> Bool
esta [] = False
esta (x:x2:xs) = (x==x2) || esta(x2:xs) 

pertenece :: [Int]->Int-> Bool
pertenece []_ = False
pertenece (x:xs) y = (x==y) || pertenece xs y

borrar :: Int -> [Int] -> [Int]
borrar _[] = []
borrar x (y:ys) = if x == y then ys else x:(borrar x ys)

-- x: ... ese elemento más borrar el resto de la lista 