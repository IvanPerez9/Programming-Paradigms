module HojaEjercicios.RepasoHojaES2 where

import Data.Char

{-
Funcion que dado un listado de nombres lo muestre por pantalla en forma de tabla.
> escribeTabla ["pepe","caramelo","lluvia"]
1: pepe
2: caramelo
3: lluvia
-}

escribeTabla :: [String] -> IO()
escribeTabla lista = escribeTablaAux lista 1

escribeTablaAux :: [String] -> Int -> IO()
escribeTablaAux [] _ = return()
escribeTablaAux (l:ls) cont = do
							 print (show cont ++ "." ++ l)
							 escribeTablaAux ls (cont+1 )

{-
Definir una funcion que sea capaz de leer dos lineas de la entrada estandar y las
compare, escribiendo una cadena por pantalla que indique si son iguales o no. 
-}

ejercicioB :: IO()
ejercicioB = do
			 print ("Escriba la primera linea")
			 linea1 <- getLine
			 print ("Escriba la segunda linea")
			 linea2 <- getLine
			 let a = comparar linea1 linea2
			 if a then print ("Son iguales") else print ("No son iguales") 
			 
			 
comparar :: String -> String -> Bool
comparar [] [] = True
comparar [] _ = False
comparar _ [] = False
comparar (c:cs) (l:ls) =  c==l && comparar cs ls

{-
Definir una funcion que lea el contenido de un fichero de texto, lo procese
invirtiendo todo el contenido y lo escriba de nuevo sobre el mismo fichero de
entrada. 
-}

ejercicioC :: IO()
ejercicioC = do
			print ("URL del fichero de entrada")
			file1 <- getLine
			print ("URL del fichero salida") 
			file2 <- getLine
			leer <- readFile file1
			let fileX = invertir file1
			writeFile file2 fileX
			print ("Fichero escrito")
			
invertir :: String -> String
invertir [] = []
invertir lista = foldr (\x acum -> acum ++ [x] ) [] lista


{-
Definir una funcion que sea capaz de ir leyendo líneas de la entrada estandar y las
va imprimiendo junto con el número de caracteres que tienen. Se ira ejecutando
mientras no se encuentra una línea vacía. 
-}

ejercicioD :: IO()
ejercicioD = do 
			print ("Introduce una linea")
			linea <- getLine
			if (linea == []) then return()
				else do
					print ("La frase tiene " ++ show (length linea) ++ " caracteres")
					ejercicioD


-- Definir una funcion que sea capaz de copiar el contenido de un fichero en otro

ejercicioE :: IO()
ejercicioE = do
			print ("Introduce la URL del fichero de entrada")
			file1 <- getLine
			print ("Introduce la URL del fichero de salida")
			file2 <- getLine
			contenido <- readFile file1
			writeFile file2 contenido
			
