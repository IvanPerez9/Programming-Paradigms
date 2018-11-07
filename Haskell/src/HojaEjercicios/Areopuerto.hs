module HojasEjercicios.Areopuerto where

import Data.Char

 {-
    Ejercicio 5
    Aeropuerto
    show (A "Barajas" 6 200 2 ["Iberia","AirEuropa"])
    show (A "Barcelona" 6 200 2 ["Iberia","RyanAir"])
    [(A "Barcelona" 6 200 10 ["Iberia","RyanAir"]),(A "Qatar" 7 100 9 ["LineaA","LineaB"]),(A "Alemania" 6 200 8 ["LineaC","LineD"])]
 -}


type Nombre = String
type Pistas = Int
type Trafico = Int
type Accidente = Int
type Compania = String
data Aeropuerto = A Nombre Pistas Trafico Accidente [Compania]

instance Show Aeropuerto where
	show (A n p t acc com) = "Aeropuerto: " ++ n ++ " Pistas: " ++ show p ++ " Trafico: " ++ show t ++ 
							" Accidente: " ++ show acc ++ " Companias " ++ show (length com)
						
instance Eq Aeropuerto where
	(A n p t acc com) == (A n2 p2 t2 acc2 com2) = (p==p2) && (t == t2) && ((length com) == (length com2))

	
dameLista :: Aeropuerto -> [Aeropuerto] -> [Aeropuerto] 
dameLista _ [] = [] 
dameLista a (l:ls) = if (a==l) && ((dameAccidentes a) < (dameAccidentes l)) then l:dameLista a ls else dameLista a ls

dameAccidentes :: Aeropuerto -> Int
dameAccidentes  (A n1 p1 t1 a1 l1) = a1

--dameLista (A "Aero1" 3 5 2 ["Pene"] ) [(A "Aero2" 3 5 5 ["Pene"] ),(A "Aero3" 4 5 5 ["Pene"] )]

