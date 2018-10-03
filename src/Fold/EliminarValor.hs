module Fold.EliminarValor where

-- Reciva una lista de enteros y un valor, elimine ese valor de toda la lista

eliminarValor :: [Int] -> Int -> [Int]
eliminarValor lista elemento = foldr (\x acum -> if x==elemento then acum else x:acum ) [] lista

-- igual que acum ++ [x]

eliminarValor2 :: [Int] -> Int -> [Int]
eliminarValor2 lista elemento = foldr (\acum x -> if x==elemento then acum else acum++[x] ) [] lista

-- Right es de derecha a izquierda