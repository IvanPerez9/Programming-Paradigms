module Recursividad.Ternas where

-- Ternas: Recibe dos lista y haga otras lista combinando el primero de la lista 1 y los dos siguientes de la lista 2
-- Hasta que te quedes sin elementos en alguna de las listas

-- [1,2,3,4] [3,3,4,5,6,7,7,8,9] -> ( [1,3,3] , [2,4,5] , [3,6,7] , [4,7,8])


ternas :: [Int] -> [Int] -> [(Int,Int,Int)]
ternas [] _ = []
ternas _ [] = []
ternas _ [x] = []
ternas (x:xs)(y:y2:ys) = (x,y,y2):ternas xs ys

-- Con (y:ys) y luego llamas a head en vez de y2 vale tambien
-- Los dos puntos solos : , es como el tipo, que es lista en este caso

