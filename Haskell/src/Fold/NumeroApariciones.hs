module Fold.NumeroApariciones where

-- Numero de apariciones de un elemento

numeroApariciones :: [Int]->Int -> Int
numeroApariciones lista elemento = foldr (\x sumador -> if x==elemento then sumador+1 else sumador ) 0 lista

apariciones2 :: [Int]->Int->Int
apariciones2 lista elemento = foldl (\sumador x -> if x==elemento then sumador+1 else sumador) 0 lista

-- Sumador y el elemeto x de la lista