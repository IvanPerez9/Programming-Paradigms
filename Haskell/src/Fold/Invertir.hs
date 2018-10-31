module Fold.Invertir where

-- Invertir una lista que se le pasa

invertir :: [Int] -> [Int]
invertir lista = foldl(\acum x -> x:acum ) [] lista

-- l de left , con r es el normal, y este va al revés