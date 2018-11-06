module HojaEjercicios.RepasoHojaEjerciciosPlegado where

{-
d) Se piden diferentes funciones que hagan uso de la función foldr o foldl para resolver
lo siguiente:
1. Reciba una lista de enteros y devuelva la suma de sus dobles.
2. Reciba una lista de enteros y devuelva la suma de sus cuadrados.
3. Reciba una lista de enteros y un entero y lo inserte al final de dicha lista.
4. Reciba una lista y un número entero y devuelva dicha lista eliminando las
apariciones de ese número entero.
-}

--1 

ejercicioA :: [Int] -> Int
ejercicioA lista = foldl (+) 0 (map (2*) lista)

--2 

ejercicioB :: [Int] -> Int
ejercicioB lista = foldl (+) 0 (map (^2) lista)

-- 3

ejercicioC :: [Int] -> Int -> [Int]
ejercicioC lista n = foldr (\x acum -> x:acum) [n] lista

--4 

ejercicioD :: [Int] -> Int -> [Int]
ejercicioD [] _ = []
ejercicioD lista num = foldl (\acum x -> if x == num then acum else x:acum) [] lista