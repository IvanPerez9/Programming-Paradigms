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

suma ::[Int] -> Int
suma lista = foldl (+) 0 (lista)

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

{-
Implementa una función en Haskell que elimine de una lista de enteros aquellos
números múltiplo de x.
> cribar [0,5,8,9,-9,6,0,85,-12,15] 2
[5,9,-9,85,15]
Se piden diferentes versiones de la misma función:
- Con definición de listas por comprensión
- Con recursividad no final
- Con recursividad final o de cola
-}

cribar :: [Int] -> Int -> [Int]
cribar lista n = [x | x <- lista , x `mod` n /=0] 

--

cribarRecursivo :: [Int] -> Int -> [Int]
cribarRecursivo [] _ = []
cribarRecursivo (x:xs) n = if x `mod` n  /= 0 then cribar xs n else x:cribar xs n

--

cribarFinal :: [Int] -> Int -> [Int]
cribarFinal lista n = cribarAux lista n []

cribarAux :: [Int] -> Int -> [Int] -> [Int]
cribarAux [] _ acum = acum
cribarAux (x:xs) n acum = if x `mod` n /= 0 then cribarAux xs n (acum++[x]) else cribarAux xs n acum 

{-
Se pide una función polimórfica en Haskell que dado un elemento y una lista añada
dicho elemento al final de la lista.
-}

insertarFinal :: [Int] -> Int -> [Int]
insertarfinal lista n = foldr (\x acum -> x:acum) [n] lista

{-
Intercambiar dos elementos de orden en una lista
-}

intercambiar :: [Int] -> Int -> Int -> [Int]
intercambiar (x:xs) y z = if x == y then z:xs else x:(intercambiar (xs) y z)

-- Menor de una lista

menor :: [Int] -> Int
menor (l:ls) = menorAux ls l 

menorAux :: [Int] -> Int -> Int
menorAux [] n = n
menorAux (x:xs) n = if x < n then menorAux xs x else menorAux xs n
