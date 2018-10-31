module Recursividad.Posicion where

--Lista de netero y devolver una lista de duplas, con el elemento en cuestion y en la posicion en la que aparece por primera vez

-- Funcion auxiliar para pasar el acumulador 

contador :: ([Int],Int) -> Int
contador ([],acum) = 0
contador (x:xs, acum) = contador (xs, acum+1)

--posicion :: [Int] -> [(Int,Int)]
--posicion [] = []
--posicion (x:xs) = (x,contador(xs,

-- Lista original, la posicion, el control de si esta ya, y resultado
posicionAux :: [Int] -> Int -> [Int] ->[(Int,Int)] -> [(Int,Int)]
posicionAux [] _ _ res = res
posicionAux (l:ls) pos control res = if pertenece l control then posicionAux ls (pos+1) control res
									else posicionAux ls (pos+1) (l:control) (res++[(l,pos)])
									
pertenece :: Int -> [Int] -> Bool
pertenece_[] = False
pertenece x(y:ys) = (x==y) || (pertenece x ys)

-- (l:control) es meter en la lista de control el l 
