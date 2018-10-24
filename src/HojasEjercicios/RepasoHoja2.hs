module HojasEjercicios.RepasoHoja2 where

{- A)
Implementa una función en Haskell que elimine de una lista de enteros aquellos
números múltiplo de x.
> cribar [0,5,8,9,-9,6,0,85,-12,15] 2
[5,9,-9,85,15]
Se piden diferentes versiones de la misma función:
- Con definición de listas por comprensión
- Con recursividad no final
- Con recursividad final o de cola
-}

ejercicioA :: [Int] -> Int -> [Int]
ejercicioA lista num = [x | x <- lista , x `mod` num /= 0]

ejercicioA' :: [Int] -> Int -> [Int]
ejercicioA' [] _ = [] 
ejercicioA' (x:xs) num = if x `mod`num /=0 then x:ejercicioA' xs num else ejercicioA' xs num 

ejercicioA'' :: [Int] -> Int -> [Int]
ejercicioA'' (l:ls) num = ( ejercicioA2 (l:ls) num [])

ejercicioA2 :: [Int] -> Int -> [Int] -> [Int]
ejercicioA2 [] _ [] = []
ejercicioA2 (l:ls) num acum = if (l `mod`num /= 0) then ejercicioA2 ls num (l:acum) else ejercicioA2 ls num acum

{- B)
 Dada la siguiente definición de función
doble :: Int -> Int
doble x = x + x
¿Cómo cambiaría la definición utilizando expresiones lambda?
-}

doble :: Int -> Int
doble x = x + x

ejercicioB :: Int -> Int
ejercicioB x = (\n -> n*2) x -- PORQUÉ LA X POR FUERA

{- C)
Se pide una función en Haskell que dada una lista de números enteros obtenga un
número entero con el resultado de calcular el doble de cada uno de los elementos de la
lista original y sumarlos todos. Se piden diferentes versiones de la misma función:
- Con recursividad no final
- Con recursividad final o de cola
- Utilizando expresiones lambda u orden superior (se puede hacer uso de la
función predefinida de Haskell map). 
-}

ejercicioC :: [Int] -> Int
ejercicioC [] = 0
ejercicioC (l:ls) = (2*l) + ejercicioC ls 

ejercicioC' :: [Int] -> Int 
ejercicioC' (l:ls) = ejercicioCAux (l:ls) 0

ejercicioCAux:: [Int] -> Int -> Int
ejercicioCAux [] _ = 0
ejercicioCAux (l:ls) acum = ejercicioCAux ls (2*l + acum) 

ejercicioC'' :: [Int] -> Int
ejercicioC'' l = foldl (+) 0 (map (2*) l)

{- D)
Implementa una función que sume los cuadrados de los números pares contenidos en
una lista de números enteros. Se piden dos versiones:
a. Una versión que haga uso de las funciones de orden superior de listas map y
filter para definir la nueva función.
b. Una versión que utilice la definición de listas por comprensión.

 -}
 
ejercicioDa :: [Int] -> Int
ejercicioDa l = foldr (+) 0 [(x^2) | x <- l , x `mod` 2 == 0] -- Right , de derecha a izq
