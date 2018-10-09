module DefinicionTipos.ListaRacionales where

{- Se define una funcion que dada una lista de racionales donde cada racional se define como dos numeros enteros (numerador y denominador)
, y un numero racional, devuelva otra lista con todos los racionales equivalentes al dado. Realizar 2 veces
Empleando Type
Empleando Data
-}

-- Empleando Data 
type Numerador = Integer
type Denominador = Integer
data Fraccion = F Numerador Denominador deriving Show 

-- Definir por sus componentes para poder operar mejor 

equivalente :: Fraccion -> Fraccion -> Bool 
equivalente (F n1 d1) (F n2 d2) = n1 * d2 == n2 * d1 


-- lo mismo F { numerador::Numerador , denominador:: Denominador} deriving Show
-- equivalente f1 f2 = numerador f1 * denominador f2 == ... 

