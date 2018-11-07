module HojasEjercicios.EjerciciosRepaso where

import Data.Char

-- Ultima aparicion junto a la posicion en la que aparece
-- Ejercicio E de la 2 

ultimaAparicion :: [Int] -> [(Int,Int)]
ultimaAparicion lista = ultimaAparicionAux (reverse lista) (length lista) [] []

ultimaAparicionAux :: [Int] -> Int -> [Int] -> [(Int,Int)] -> [(Int,Int)]
ultimaAparicionAux [] cont vistos resultado = resultado
ultimaAparicionAux (l:ls) cont vistos resultado = if esta vistos l then ultimaAparicionAux ls (cont-1) vistos resultado
												  else ultimaAparicionAux ls (cont-1) (l:vistos) ((l,cont):resultado)



esta :: [Int] -> Int -> Bool
esta [] _ = False
esta (n:ns) e = if n == e then True else esta ns e