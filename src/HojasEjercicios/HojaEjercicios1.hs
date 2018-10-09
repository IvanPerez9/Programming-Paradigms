module HojasEjercicios.HojaEjercicios1 where

import Data.Char

-- a) Implementar una función en Haskell que dados tres números enteros determine si están
--    ordenados de menor a mayor. ejercicioA 3 4 5 

ejercicioA :: Int -> Int -> Int -> Bool 
ejercicioA x y z = if (x<y) && (y<z) then True else False

-- b) Implementar una función en Haskell que dados tres números enteros los devuelva
--    ordenados de menor a mayor. 

ejercicioB :: Int -> Int -> Int -> (Int,Int,Int)
ejercicioB x y z  
				| z>x && z>y && y>x = (x,y,z)
				| y>x && y>z && z>x = (y,z,x)
				| x>y && x>z && y>z = (z,y,x)
				| z>x && z>y && x>y = (z,x,y)
				| y>x && y>z && z<x = (y,x,z)
				| x>y && x>z && z>y = (y,z,x)
			    | otherwise =(1,1,1)
			  
-- c)  Implementar en Haskell una función que reciba un número real y devuelva una tupla
--     con su parte entera y sus dos primeros decimales (como número entero).

ejercicioC :: Double -> (Int,Int)
ejercicioC x = (truncate(x) , truncate( (x - fromInteger(truncate (x))) * 100))

-- d) Crear una función que reciba el radio de una circunferencia y devuelva una 2-tupla con
--  la longitud de la circunferencia y con el área del círculo. Emplea una definición local con
-- la cláusula where para almacenar el valor de Pi (Nota: no se debe utilizar la función
-- predefinida pi). A continuación crear una función con el mismo cometido empleando la
-- definición local let.

ejercicioD :: Double -> (Double,Double)
ejercicioD x = (pi*x*x , pi * x*x) where pi = 3.14

ejercicioD' :: Double -> (Double,Double)
ejercicioD' x = let pi =3.14 in (pi*x*x, pi*x*x)

-- e) Implementar la función predefinida de listas concat, que se llamará concatenar,
-- utilizando la definición de listas por comprensión (no se puede utilizar recursividad).

--ejercicioE :: [Int] -> [Int] -> [Int]
--ejercicioE x:xs y:ys = 

-- f) Implementar una función que dado un número entero devuelva en una lista todos los
-- factores de dicho número. Se debe utilizar la definición de listas por comprensión. 

ejercicioF :: Int -> [Int]
ejercicioF x = [ y | y <- [1..x] , x `mod` y == 0]

-- h) Implementar una función que diga cuántos caracteres en mayúscula están contenidos
-- en una frase dada. Se deberá utilizar la definición de listas por comprensión. 

ejercicioH :: String -> Int
ejercicioH s = length [c | c <- s, isUpper c]

-- i) Implementar una función que dada una tupla de tres elementos, donde cada uno de
-- ellos es a su vez una tupla de dos elementos de tipo String e Int respectivamente,
--retorne el primer elemento de cada tupla interna. Se deberá utilizar ajuste de patrones. 

ejercicioI :: ((String,Int),(String,Int),(String,Int)) -> (String,String,String)
ejercicioI ((s,_),(d,_),(f,_)) = (s,d,f)

-- j)  Implementar una función que devuelve True si la suma de los cuatro primeros
-- elementos de una lista de números enteros es un valor menor a 10 y devolverá False
-- en caso contrario. Se deberá utilizar ajuste de patrones.

ejercicioJ :: [Int] -> Bool
ejercicioJ [x,y,z,t] = if (x+y+z+t) < 10 then True else False
ejercicioJ [] = False

-- k) Implementar una función que dado un carácter, que representa un punto cardinal,
-- devuelva su descripción. Por ejemplo, dado ‘N’ devuelva “Norte”.

{- ejercicioK :: Char -> String
ejercicioK c
			| 'N' = "Norte"
			| 'S' = "Sur"
			| 'O' = "Oeste"
			| 'E' = "Este"
			| otherwise "MAL"  
			-}
			
			
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
ejercicioL "" = "Cadena Vacia"
ejercicioL s = "La primera letra de la frase" ++ s ++ "es" ++ [head s] ++ "Y la ultima es: " ++ [last s]


-- m) Implementar una función que dado un número entero devuelva mensajes indicando en
-- qué rango de valores se encuentra dicho número (menor de 10, entre 10 y 20 o mayor
-- de 20). Se debe utilizar definiciones locales.

ejercicioM :: Int -> String
ejercicioM x
			| x< 10 = cad ++ "menor de 10"
			| x<= 20 = cad ++ "entre 10 y 20"
			| x >20 = cad ++ "mayor de 20"
			where cad = "El valor de entrada es "
			
-- n) Implementar una función que dada una cadena de caracteres y un carácter, indique el
-- número de apariciones del carácter en la cadena. No se debe utilizar recursividad, sí
-- ajuste de patrones. Pista: utilizar la definición de listas por comprensión.

ejercicioN :: String -> Char -> Int
ejercicioN ""_ = 0
ejercicioN s c = length [t | t <- s, t == c]