module Fold.EliminarMultiplos where

-- Lista de multiplos de un numero y los elimine

eliminarMultiplos :: [Int]->Int -> [Int]
eliminarMultiplos lista elemento = foldr(\x acum -> if (x`mod`elemento ==0) then acum else x:acum) [] lista

-- Depende de si vas por la izqu o derecha, representa el primer parametro a los elementos de la lista o el acumulador



