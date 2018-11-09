module HojaEjercicios.Examen where

import Data.Char

{-
Una de las principales preocupaciones de los estudiantes que deciden venir de otras regiones a estudiar a la URJC es encontrar un alojamiento para poder pasar el curso. La Universidad, en su afán de facilitar dicha tarea a sus alumnos, ha decidido crear un repositorio de pisos de alquiler. De dichos pisos la información que maneja la URJC es: dirección, distancia respecto a la Universidad, precio del alquiler mensual y capacidad. En cuanto a la capacidad, los mismos se caracterizan por el número de habitaciones individuales y dobles de que dispone cada piso.

Define un tipo de dato adecuado para gestionar este tipo de alojamiento universitario. (0.5 puntos)
Implementa todo lo que consideres necesario para poder comparar pisos. Un piso es igual a otro si tiene la misma ratio precio/persona. Un piso es mejor que otro si su precio por persona es más barato. En caso de tener igual esta ratio, será mejor aquel que se encuentre más cerca de la Uni (2 puntos)
Implementa todo lo necesario para que la información de un piso salga por pantalla de una manera apropiada, dando todos los datos relativos a sus características de una manera apropiada para el alumno que quiera consultar la misma (1.5 puntos)
-}

data Capacidad = Capac{ individuales:: Int,
           dobles:: Int}

data Piso = P { direccion :: String,
          distancia :: Int,
          precio :: Int,
          capacidad :: Capacidad} 
          
instance Eq Piso where
  (==) (P _ _ p1 (Capac i1 d1)) (P _ _ p2 (Capac i2 d2)) = p1 div (i1 + (2*d1)) == p2 div (i2 + (2*d2))
  (/=) p1 p2 = not (p1 == p2)
  
instance Ord Piso where
  (>) (P _ d1 p1 (Capac i1 do1)) (P _ d2 p2 (Capac i2 do2)) = p1 div (i1 + (2*do1)) < p2 div (i2 + (2*do2)) || (p1 div (i1 + (2*do1)) == p2 div (i2 + (2*do2)) && (d1 < d2))
  (<=) p1 p2 = not (p1 > p2)
  (<) (P _ d1 p1 (Capac i1 do1)) (P _ d2 p2 (Capac i2 do2)) = p1 div (i1 + (2*do1)) > p2 div (i2 + (2*do2)) || (p1 div (i1 + (2*do1)) == p2 div (i2 + (2*do2)) && (d1 > d2))
  
  
instance Show Piso where
  show (P dir dis precio capacidad) = "Direccion: " ++ dir ++ " | Distancia: " ++ show dis ++ " | Precio: " 
    ++ show precio ++ " euros. " ++ show capacidad
  
instance Show Capacidad where
  show (Capac ind dobles) = " | Capacidad del piso: " ++ show ind ++ " habitaciones individuales y " 
    ++ show dobles ++ " habitaciones dobles."

--para pruebas

anadirPiso :: Piso -> [Piso] -> [Piso]
anadirPiso p1 [] = [p1]
anadirPiso p1 x = p1:x

piso1:: Piso
piso1 = P "Calle calle" 20 300 (Capac 2 3)

piso2:: Piso
piso2 = P "Calle piruleta" 10 300 (Capac 2 3)

piso3:: Piso
piso3 = P "Calle Alfonso" 7 700 (Capac 2 2)



--Implementa una función polimórfica con la instrucción fold que reciba una lista de duplas
-- y devuelva una dupla de listas, donde en la primera lista aparezcan los elementos que 
--forman la primera componente de las duplas y en la segunda lista los elementos de 
--la segunda componente de las duplas (1 punto)

duplaLista:: (Ord a)=>[(a,a)] -> ([a],[a])
duplaLista ((x,y):xs) = foldr (\ (z,y) (zs,ys) -> (z:zs, y:ys)) ([x],[y]) xs

{-
Escribe un programa en Haskell que lea un archivo de texto, separe el contenido del mismo por frases
 (separadas por puntos) y reescriba su contenido en dos archivos diferentes, pero separando de manera 
 alternativa cada una de las frases del texto original en cada uno de los archivos.
 Para realizar este ejercicio está prohibido hacer uso de la función split ni de ninguna de sus variantes
-}

ejercicioC :: IO()
ejercicioC = do
			print ("introduce el nombre del archivo")
			file1 <- getLine
			print ("Introduce el archivo 1 donde quieres escribir")
			fileOut1 <- getLine
			print ("Introduce el archivo 2 donde quieres escribir")
			fileOut2 <- getLine
			contenido <- readFile file1
			if contenido 