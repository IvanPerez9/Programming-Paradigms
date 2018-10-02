module Recursividad.InsertarFinalLista where


-- Insertar un elemento al final de la lista

insertarFinalLista :: [Int]->Int -> [Int]
insertarFinalLista lista elemento = foldr (\x acum-> x:acum) [elemento] lista


-- Numero de apariciones de un elemento

apariciones :: [Int]->Int->Int
apariciones lista elemento = foldl (\sumador x -> if x==elemento then sumador+1 else sumador) 0 lista

-- Sumador y el elemeto x de la lista