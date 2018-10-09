module HojasEjercicios.HojaEjercicios2 where

-- Implementa una función en Haskell que elimine de una lista de enteros aquellos
-- números múltiplo de x. Va con Listas por compresion (Forma de recorrer las listas)

ejercicioA :: [Int]-> Int -> [Int]
ejercicioA lista x = [c | c <- lista , c `mod` x /= 0 ]

-- Con recursividad no final 

ejercicioA' :: [Int] -> Int -> [Int]
ejercicioA' []_ = []
ejercicioA' (l:ls) x = if l `mod` x /= 0 then l:ejercicioA' ls x else ejercicioA' ls x

-- Con recursividad final o de cola
{-
ejercicioA'' :: [Int] -> Int -> [Int]
ejercicioA'' []_ = []
ejercicioA'' (l:ls) x = if
-}

{- Dada la siguiente definición de función
doble :: Int -> Int
doble x = x + x
¿Cómo cambiaría la definición utilizando expresiones lambda?
-}

ejercicioB :: Int -> Int
ejercicioB x = x

{- Se pide una función en Haskell que dada una lista de números enteros obtenga un
número entero con el resultado de calcular el doble de cada uno de los elementos de la
lista original y sumarlos todos. Se piden diferentes versiones de la misma función:
- Con recursividad no final
- Con recursividad final o de cola
- Utilizando expresiones lambda u orden superior (se puede hacer uso de la
función predefinida de Haskell map). -}

ejercicioC :: [Int] -> Int
ejercicioC [] = 0
ejercicioC (l:ls) = (2*l) + ejercicioC ls -- Porque no 2*l : ejercicioC ls 

ejercicioC' :: [Int] -> Int
ejercicioC' [] = 0
ejercicioC' l = ejercicioCAux l 0 -- Le paso la lista y la acumulacion de sumarlos 

ejercicioCAux :: [Int] -> Int -> Int
ejercicioCAux (n:ns) acum = ejercicioCAux ns (2*n + acum) 

-- Con expresion lamda
{-
ejercicioC'' :: [Int] -> Int 
ejercicioC'' lista = map ((*2) lista)
-}

{- Implementa una función que sume los cuadrados de los números pares contenidos en
una lista de números enteros. Se piden dos versiones:
a. Una versión que haga uso de las funciones de orden superior de listas map y
filter para definir la nueva función.
b. Una versión que utilice la definición de listas por comprensión.
-}

ejercicioD :: [Int] -> Int
ejercicioD l = [ t | t <- l , if t `mod` 2 == 0 then 
    
    
    
 