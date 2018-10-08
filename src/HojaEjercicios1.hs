module HojaEjercicios1 where

-- a) Implementar una función en Haskell que dados tres números enteros determine si están
--    ordenados de menor a mayor. 

ejercicioA :: Int -> Int -> Int -> Bool 
ejercicioA x y z = if x<y && y<z then True else False