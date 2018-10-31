module Patrones where

import Data.Char;

-- Ejercicio 1 de la segunda parte

-- Dada una tupla de tres elementos, donde cada uno es una tupla de dos elementos de String e Int 
-- Retorne el primer elemento de cada tupla interna. Con ajuste de patrones

patrones :: ((String, Int),(String, Int),(String, Int)) -> (String,String,String)
patrones ((a,b),(c,d),(e,f))=(a,c,e)
