module HojasEjercicios.Cribar where

import Data.Char

-- Lista de enteros y un numero, dice los multiplos

cribar :: [Int] -> Int -> [Int]
cribar lista num = foldl (\acum x ->if x `mod` num ==0 then x:acum else acum ) [] lista

{-
Se piden diferentes versiones de la misma función:
- Con definición de listas por comprensión
- Con recursividad no final
- Con recursividad final o de cola
-}

cribar1 :: [Int] -> Int -> [Int]
cribar1 lista num = [x | x <- lista, x `mod` num == 0]

--

cribar2 :: [Int] -> Int -> [Int]
cribar2 [] _ = []
cribar2 (l:ls) num = if l `mod` num /= 0 then cribar2 ls num else l:cribar2 ls num

-- 

cribar3:: [Int] -> Int -> [Int]
cribar3 lista num = cribarAux lista num []

cribarAux :: [Int] -> Int -> [Int] -> [Int]
cribarAux [] _ acum = acum
cribarAux (l:ls) num acum = if l `mod` num /= 0 then cribarAux ls num acum else cribarAux ls num (l:acum)
