module Cadena where

import Data.Char

-- Ejercicio n de la 2 
-- Dada una cadena de caracteres y un solo caracter, indique el numero de apariciones del caracter en la cadena
-- Con ajuste de patrones, utilizar listas por compresion 

cadena :: String -> Char -> Int
cadena []_ = 0
cadena s c = length [x | x<-s , x == c]

-- Recorrer el Strign con lista de compresion, y devolver la lista pero su longitud
-- lista por compresion devuelve otra lista

-- cadena "Gol del Girona" 'G' 