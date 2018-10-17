module HojasEjercicios.HojaEjerciciosPlegado where

{-
d) Se piden diferentes funciones que hagan uso de la función foldr o foldl para resolver
lo siguiente:
1. Reciba una lista de enteros y devuelva la suma de sus dobles.
2. Reciba una lista de enteros y devuelva la suma de sus cuadrados.
3. Reciba una lista de enteros y un entero y lo inserte al final de dicha lista.
4. Reciba una lista y un número entero y devuelva dicha lista eliminando las
apariciones de ese número entero.
-}

-- 1.

sumaDoble :: [Int] -> Int
sumaDoble lista = foldl (+) 0 (map(*2) lista)

-- 2.

sumaCuadrado :: [Int] -> Int
sumaCuadrado lista = foldl (+) 1 (map(^2) lista)

-- 4 

eliminarApariciones :: [Int] -> Int -> [Int]
eliminarApariciones lista n = foldl (\acum x -> if (x==n)then acum else acum++[x]) [] lista

-- 3 

insertarFinal :: [Int] -> Int -> [Int]
insertarFinal lista n = foldr (\x acum -> x:acum) [n] lista

insertarFinal' :: [Int] -> Int -> [Int]
insertarFinal' lista n = foldr (:) [n] lista
