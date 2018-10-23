module HojasEjercicios.RepasoHoja1 where

import Data.Char

-- a) Implementar una función en Haskell que dados tres números enteros determine si están
--    ordenados de menor a mayor. ejercicioA 3 4 5 

ejercicioA :: Int -> Int -> Int -> Bool
ejercicioA x y z = x<y && y>z

-- b) Implementar una función en Haskell que dados tres números enteros los devuelva
--    ordenados de menor a mayor

ejercicioB :: Int -> Int -> Int -> (Int,Int,Int)
ejercicioB x y z = if (x>y) then ejercicioB y x z
					else if (y>z) then ejercicioB x z y
					else (x,y,z)

-- c)  Implementar en Haskell una función que reciba un número real y devuelva una tupla
--     con su parte entera y sus dos primeros decimales (como número entero).

ejercicioC :: Double -> (Int , Int)
ejercicioC num = (truncate num, truncate (num - fromInteger (truncate num))* 100)

-- d) Crear una función que reciba el radio de una circunferencia y devuelva una 2-tupla con
--  la longitud de la circunferencia y con el área del círculo. Emplea una definición local con
-- la cláusula where para almacenar el valor de Pi (Nota: no se debe utilizar la función
-- predefinida pi). A continuación crear una función con el mismo cometido empleando la
-- definición local let.

ejercicioD :: Double -> (Double ,Double)
ejercicioD radio = (2*pi*radio,pi*radio*radio) where pi = 3.14

ejercicioD' :: Double -> (Double,Double)
ejercicioD' radio = let pi = 3.14 in (2*pi*radio,pi*radio*radio)

-- e) Implementar la función predefinida de listas concat, que se llamará concatenar,
-- utilizando la definición de listas por comprensión (no se puede utilizar recursividad).

ejercicioE :: [[Int]] -> [Int]
ejercicioE l = [x | y <- l , x <- y]

-- f) Implementar una función que dado un número entero devuelva en una lista todos los
-- factores de dicho número. Se debe utilizar la definición de listas por comprensión. 

ejercicioF :: Int -> [Int]
ejercicioF num = [ y | y <- [1..num] , num `mod` y == 0]

{-
 g) Implementar una funcion que diga si un numero es primo. Para ello se debe
utilizar la funcion que calcula el numero de factores de un numero . Utilizando ejercicio F
-}

ejercicioG :: Int -> Bool
ejercicioG num = length (ejercicioF num) < 3

-- h) Implementar una función que diga cuántos caracteres en mayúscula están contenidos
-- en una frase dada. Se deberá utilizar la definición de listas por comprensión. 

ejercicioH :: String -> Int
ejercicioH s = length [x | x <- s , isUpper x]

-- i) Implementar una función que dada una tupla de tres elementos, donde cada uno de
-- ellos es a su vez una tupla de dos elementos de tipo String e Int respectivamente,
--retorne el primer elemento de cada tupla interna. Se deberá utilizar ajuste de patrones. 

ejercicioI :: ((String,Int),(String,Int),(String,Int)) -> (String,String,String)
ejercicioI ((s,_),(t,_),(k,_)) = (s,t,k)

-- j)  Implementar una función que devuelve True si la suma de los cuatro primeros
-- elementos de una lista de números enteros es un valor menor a 10 y devolverá False
-- en caso contrario. Se deberá utilizar ajuste de patrones.

ejercicioJ :: [Int] -> Bool
ejercicioJ [x,y,z,t] = (x+y+z+t) > 10

-- k) Implementar una función que dado un carácter, que representa un punto cardinal,
-- devuelva su descripción. Por ejemplo, dado ‘N’ devuelva “Norte”.

{-
ejercicioK :: Char -> String
ejercicioK c = 
			  |'N' = "Norte"
			  |'S' = "Sur" 
			  |'E' = "Este"
			  |'O' = "Oeste" 
			  |otherwise "MAL"
-}		  
ejercicioK' :: Char -> String
ejercicioK' 'N' = "Norte"
ejercicioK' 'S' = "Sur"
ejercicioK' 'E' = "Este"
ejercicioK' 'O' = "Oeste"
ejercicioK' ' ' = "Mal."


-- l) Implementar una función que dada una frase retorne un mensaje donde se indique cuál
-- es la primera y última letra de la frase original. Un ejemplo de aplicación de la función
-- podría ser
--  Se debe usar ajuste de patrones y se puede utilizar también patrones nombrados

{-
> procesarFrase "El perro de San Roque"
"La primera letra de la frase ''El perro de San Roque'' es 'E' y la
ultima letra es 'e'"
-}

ejercicioL :: String -> String
ejercicioL frase = "La primera letra es: " ++ [head frase] ++ "La ultima frase es: " ++ [last frase] 


-- m) Implementar una función que dado un número entero devuelva mensajes indicando en
-- qué rango de valores se encuentra dicho número (menor de 10, entre 10 y 20 o mayor
-- de 20). Se debe utilizar definiciones locales.

ejercicioM :: Int -> String
ejercicioM num 
				| num < 10 = "Es menor que 10" 
				| num < 20 = "Esta entre 10 y 20" 
				| num > 20 = "Es mayor de 20" 
				
-- n) Implementar una función que dada una cadena de caracteres y un carácter, indique el
-- número de apariciones del carácter en la cadena. No se debe utilizar recursividad, sí
-- ajuste de patrones. Pista: utilizar la definición de listas por comprensión.

ejercicioN:: String -> Char -> Int
ejercicioN s c = length [x| x<-s , c == x ]