module Fold.InsertarFinalLista where

-- Insertar un elemento al final de la lista 

insertarFinal :: [Int]->Int -> [Int]
insertarFinal lista elemento = foldr (\x acum -> x:acum ) [elemento] lista 

-- r (right) de derecha a izquierda 
-- x elementos de la lista
-- Acumulador, el final 

-- Si es l (left) van al revés, acum en la \ y elementos de la lista fuera