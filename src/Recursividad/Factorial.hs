module Recursividad.Factorial where

import Data.Char;

factorial:: Int -> Int
factorial n = if n == 0 then 1 else n * factorial(n-1)

-- facotrial 0 = 1
-- factorial n = n * factorial (n-1) 

-- Factorial como recursividad final

fact :: (Int, Int) -> Int
fact (n,r) = if n == 1 then r else fact(n-1,r*n)

-- fact(4)  fact2(4,1)  fact2(3,4)  fact2(2,12) fact2(1,24)  24