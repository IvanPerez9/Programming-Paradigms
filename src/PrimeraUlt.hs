module PrimeraUlt where

import Data.Char;

-- Ejercicio l de la 2 
-- Implementar una funcion que data una frase retorne el mensaje donde se indique la primera y la ultima letra de la frase
-- Con mensajes como "La primera letra de la frase" "x" es: y la ultima es:

primeraUlt :: String -> String
primeraUlt s = "La primera letra de la frase " ++ s ++ " es: "++ [head s] ++ "Y la ultima es: "++ [last s] 


-- Los pones entre corchetes y se convierte en una lista 
