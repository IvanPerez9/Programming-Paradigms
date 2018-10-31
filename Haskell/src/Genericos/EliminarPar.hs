module Genericos.EliminarPar where

-- Eliminar en la poscion par el numero que haya 

-- Como te devuelve resultado y desecho, tu quitas el que no quieres
-- Programa de atras a delante
eliminarPar :: [a] -> [a]
eliminarPar lista = resultado where (resultado,desecho) = eliminarParAux lista


-- Caso base, la lista vacia, y porque posicion voy
-- Acum es el elemento y x la lista resultado
eliminarParAux :: [a] -> ([a],Int)
eliminarParAux lista = foldl (\(acum,pos) x -> if even pos then (acum,pos+1) else (acum ++ [x], pos +1))([],0) lista 

-- Acumuklador y un contador


borrar :: Int -> [Int] -> [Int]
borrar _[] = []
borrar x (y:ys) = if x == y then ys else x:(borrar x ys) 