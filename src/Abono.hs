module Abono where

import Data.Char;

-- GUARDAS
-- El abono de menores de 10 y mayores de 65 el valor es 0€
-- Si estas entre 10-25 entonces 20€
-- Si tienes entre 25-65 entonces 100€

abonoPrecio :: Int -> Int
abonoPrecio x 
	| x < 10 = 0
	| x < 25 = 20
	| x < 65 = 100
	| otherwise = 0;