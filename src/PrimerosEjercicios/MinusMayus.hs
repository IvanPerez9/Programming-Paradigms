module MinusMayus where

import Data.Char;

-- 1. Que cambie las mayusculas por minusculas y las mayusculas por minusculas

-- Despues de la coma es como un 'if' 


minusMayus :: String -> String
minusMayus s = [if isUpper l then toLower l else toUpper l | l <- s] -- Recorre la lista 
			
			
			
-- | [c | c <- s , isUpper c] = mayusculas s
--			| otherwise = minusculas s
			
--mayusculas :: Char -> Char 
--mayusculas x = toUpper x

--minusculas :: Char -> Char 
--minusculas x = toLower x



-- 	if s >= 'A' && s <= 'Z'
--	then toLower s
--	else toUpper s