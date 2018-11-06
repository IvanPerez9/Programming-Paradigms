module HojasEjercicios.HojaEjercicios3 where

{-
Se pide una función que dada una lista de racionales, donde cada racional se define como
dos números enteros (numerador y denominador), y un número racional, devuelva otra
lista con todos los racionales equivalentes al dado. Realiza dos versiones del ejercicio:
1. Empleando type.
2. Empleando data. 
-}

type Numerador = Integer
type Denominador = Integer
type Fraccion = (Numerador , Denominador) 

data Racional = R (Numerador,Denominador) deriving Show

ejercicioA :: [Fraccion] -> Fraccion -> [Fraccion]
ejercicioA [] _ = []
ejercicioA lista (n,d) = foldr (\(n2,d2) acum -> if ((n*d2) == (d*n2)) then (n2,d2):acum else acum) [] lista

ejercicioA' :: [Racional] -> Racional -> [Racional]
ejercicioA' [] _ = []
ejercicioA' lista (R(n,d)) = foldr (\(R(n2,d2)) acum -> if ((n*d2) == (d*n2))  then (R(n2,d2)):acum else acum) [] lista

{-
Función que dado un punto de coordenadas y una dirección (Norte, Sur, Este u
Oeste) mueva el punto hacia la dirección indicada. 
-}

type CoordenadaX = Integer 
type CoordenadaY = Integer
data Coordenadas = C CoordenadaX CoordenadaY deriving Show 
data Direccion = Norte | Sur | Este | Oeste

ejercicioB :: Coordenadas -> Direccion -> Coordenadas
ejercicioB (C x y) Norte = C (x+1) y
ejercicioB (C x y) Sur = C (x-1) y
ejercicioB (C x y) Este = C x (y+1)
ejercicioB (C x y) Oeste = C x (y-1)

-- Función que dados dos puntos de coordenadas indique cuál está más al sur

ejercicioB' :: Coordenadas -> Coordenadas -> Coordenadas
ejercicioB' (C x1 y1) (C x2 y2) = if (x2<x1) then (C x2 y2) else (C x1 y1)

-- Función que calcule la distancia entre dos puntos

type Punto = (Float,Float)

ejercicioB'' :: Punto -> Punto -> Float
ejercicioB'' (x1,y1) (x2,y2) = sqrt ( ((x2-x1)^2) + ((y2-y1)^2 ))


-- Función que dado un punto y una lista de direcciones, retorne el camino que
--forman todos los puntos después de cada movimiento sucesivo desde el punto original
{- camino (3.2,5.5) ["Sur","Este","Este","Norte","Oeste"] 
    => [(3.2,4.5),(4.2,4.5),(5.2,4.5),(5.2,5.5),(4.2,5.5)]
-}

ejercicioB4 :: Punto -> [Direccion] -> [Punto]
ejercicioB4 _ [] = []
--ejercicioB4 p (c:cs) = ejercicioB (p,c):ejercicioB4 (ejercicioB (p,c)cs) 

{- 
Definir una función que dado un día de la semana, indique si éste es o no laborable. Para
representar el día de la semana se deberá crear un nuevo tipo enumerado. 
-}

data DiaSemana = Lunes | Martes | Miercoles | Jueves | Viernes | Sabado | Domingo deriving Eq

ejercicioC :: DiaSemana -> Bool
ejercicioC x = x == Sabado || x == Domingo 

{- 
La empresa RealTimeSolutions, Inc. está trabajando en un controlador para una central
domótica. El controlador recibe información de termostatos situados en diferentes
habitaciones de la vivienda y basándose en esta información, activa o desactiva el aire
acondicionado en cada una de las habitaciones. Los termostatos pueden enviar la
información sobre la temperatura en grados Celsius o Fahrenheit. A su vez, los aparatos de
aire acondicionado reciben dos tipos de órdenes: apagar y encender (on y off). Se pide:

	1. Definir un tipo de datos para representar las temperaturas en ambos tipos de
	unidades.
	2. Definir una función convert que dada una temperatura en grados Celsius la
	convierta a grados Fahrenheit y viceversa. (Conversión de C a F: f = c * 9/5 + 32;
	conversión de F a C: c = (f – 32) * 5/9.)
	3. Definir un tipo de datos para representar las órdenes a los aparatos de a/a.
	4. Definir una función action que dada una temperatura en cierta habitación
	determine la acción a realizar sobre el aparato de a/a de dicha habitación. El
	controlador debe encender el aparato si la temperatura excede de 28ºC. Ejemplos
	de aplicación:
	> action(Celsius(25)) > action(Fahrenheit(83.5))
	On 
-}

--1
type Celcius = Float
type Fahrenheit = Float
data Temperatura = T Celcius | Farenheit deriving Show

--2
--ejercicioD2 :: Temperatura -> Temperatura
--ejercicioD2 T temp = T (temp * (9/5) + 32)

data Temperatura2 = Celsius Float | Fahrenheit Float deriving Show
convert ::  Temperatura2 -> Temperatura2 
convert (Celsius c) = Fahrenheit (c * (9/5) + 32)

--3 

data AA = Apagado | Encendido 

--4 

action :: Temperatura2 -> AA
action (Celsius c) = if c > 28 then Encendido else Apagado 

{-
Definir un tipo moneda para representar euros y dólares USA. Definir una función que
convierta entre ambas monedas sabiendo que el factor de conversión de euros a dólares
es 1.14
-}

data Moneda = Dollar Float | Euro Float

conversion :: Moneda -> Moneda 
conversion (Euro e) = Dollar (e * 1.14)
conversion (Dollar d) = Euro (d / 1.14) 

{-  Ejercicio F

Dada el siguiente tipo de datos recursivo que representa expresiones aritméticas:
data Expr = Valor Integer
|Expr :+: Expr
|Expr :-: Expr
|Expr :*: Expr deriving Show
e.1) Se pide una función para calcular el valor de una expresión.
e.2) Se pide una función para calcular el número de constantes de una expresión
-}

data Expr = Valor Integer
	|Expr :+: Expr
	|Expr :-: Expr
	|Expr :*: Expr deriving Show

-- 1

valor :: Expr -> Integer
valor (Valor x) = x

valor (exp1 :+: exp2) = valor exp1 + valor exp2 
valor (exp1 :-: exp2) = valor exp1 - valor exp2
valor (exp1 :*: exp2) = valor exp1 * valor exp2

