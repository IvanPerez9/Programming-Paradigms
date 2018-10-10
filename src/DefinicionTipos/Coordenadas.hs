module DefinicionTipos.Coordenadas where

-- Ejercicio Hoja 3 b)

{- Función que dado un punto de coordenadas y una dirección (Norte, Sur, Este u
Oeste) mueva el punto hacia la dirección indicada. Un ejemplo de aplicación de la
función sería:
-}

type CoordenadaX = Integer
type CoordenadaY = Integer
data Coordenadas = Punto CoordenadaX CoordenadaY deriving Show
data Direccion = Norte | Sur | Este | Oeste deriving Show

-- Porque punto
-- Es un constructor de datos

mover ::  Direccion -> Coordenadas -> Coordenadas 
mover Norte (Punto x y) = Punto x (y+1)
mover Sur (Punto x y) = Punto x (y-1)
mover Este (Punto x y) = Punto (x+1) y
mover Oeste (Punto x y) = Punto (x-1) y

-- Función que dados dos puntos de coordenadas indique cuál está más al sur.

masAlSur :: Coordenadas -> Coordenadas -> Coordenadas
masAlSur (Punto x1 y1) (Punto x2 y2) = if (y1<y2) then (Punto x1 y1) else (Punto x2 y2)

-- Función que calcule la distancia entre dos puntos:

distancia :: Coordenadas -> Coordenadas -> Float
distancia (Punto x1 y1) (Punto x2 y2) = sqrt(fromInteger((x1-x2)^2) + fromInteger((y1-y2)^2))