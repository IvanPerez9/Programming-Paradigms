module Recursividad.MergeSort where

import Data.Char

--mergeSort :: Divide y venceras
-- Sacas dos listas, y ordanas esas dos listas partiendolas otra vez y ordenando despues
-- Primero partir, y luego ordena y unir 
-- Uni elemento a elemento de cada lista, para hacer la superlista

mergeSort :: [Int] -> [Int]
mergeSort [] = []
merSort [x] = [x]
mergeSort l = fusionar(mergeSort a)(mergeSort b)
			  where 
			  (a,b) = partir l [](length l `div` 2)
			  
partir :: [Int]-> [Int] ->Int -> ([Int],[Int])
-- Lista vacia como acumulador más el contador que es la longitud de la lista, así divides en 2 listas
-- La mitad de la lista en la vacia y lo que me queda de la original es la otra mitad 
partir resto acum 0 = ([acum][resto])
partir (x:xs) acum long = partir xs (acum++[x]) (long-1)

fusionar :: [Int]->[Int] -> [Int]
fusionar l [] = l
fusionar [] l = l
fusionar (x:xs)(y:ys) = if (x<y) then (x:(fusionar xs(y:ys))) else (y:(fusionar (x:xs)ys))