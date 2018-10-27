module Fold.MayorTres where


-- n Mayor 3 [1,3,4,5,7] la lista con los 3 mayores -- Con recursividad normal 

mayorTres :: [Int] -> Int -> [Int]
mayorTres l n = nmayoresAux l n 0 []

-- La lista, el numero que quiero coger, numero de elementos en la lista, y lista resultados
nmayoresAux :: [Int]-> Int -> Int -> [Int] -> [Int]
nmayoresAux [] _ _ acum = acum
nmayoresAux (x:xs) n cont acum = if cont<n then nmayoresAux xs n (cont+1) (acum++[x])
								 else let a = menor (acum) in
								 	if x < a then nmayoresAux xs n cont acum
								 	else nmayoresAux xs n cont (intercambiar acum a x) -- Si es x>a 
-- Dos funciones auxiliares, una para cambiar un elemento por otro, y otra para decir cual es el menor

-- 
menor :: [Int] -> Int
menor [x]= x
menor (x:xs) = menorAux xs x -- Cojo el primero y miro 

menorAux :: [Int] -> Int ->Int
menorAux [] x = x
menorAux (y:ys) x = if y < x then menorAux ys y else menorAux ys x 

-- Intercambiar un elemento por otro 
intercambiar:: [Int] -> Int -> Int -> [Int]
intercambiar (x:xs) y z = if x==y then (z:xs) else x:(intercambiar xs z y)