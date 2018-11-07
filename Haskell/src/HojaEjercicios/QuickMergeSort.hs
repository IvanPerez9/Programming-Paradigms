module HojasEjercicios.QuickMergeSort where

import Data.Char

quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort (l:ls) = quicksort [x | x <- ls , x < l] ++ [l] ++ quicksort [y | y <- ls , y >= l]

mergeSort :: [Int] -> [Int]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort lista = fusionar (mergeSort (a)) (mergeSort (b))
				  where (a,b) = dividir lista (length lista `div` 2) []


-- Dividir la lista en 2, por la mitad

dividir :: [Int] -> Int -> [Int] -> ([Int],[Int])
dividir lista 0 acum = (acum,lista)
dividir (l:ls) long acum = dividir ls (long-1) (acum++[l])

-- Fusiono dos listas en 1 , de menor a mayor
fusionar :: [Int] -> [Int] -> [Int]
fusionar [] l = l
fusionar l [] = l
fusionar (x:xs) (y:ys) = if x < y then x:(fusionar xs (y:ys)) else y:(fusionar (x:xs) ys)