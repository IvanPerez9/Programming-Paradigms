module HojaEjercicios.RepasoHojaES2 where

import Data.Char

{-
Funcion que dado un listado de nombres lo muestre por pantalla en forma de tabla.
> escribeTabla ["pepe","caramelo","lluvia"]
1: pepe
2: caramelo
3: lluvia
-}

ejercicioA :: [String] -> IO()
ejercicioA lista = ejercicioAaux lista 1

ejercicioAaux :: [String] -> Int -> IO()
ejercicioAaux [] contador = return()
ejercicioAaux (c:cs) contador = do
						print (show contador ++ "." ++ c)
						ejercicioAaux cs (contador+1)


{-
Definir una funcion que sea capaz de leer dos lineas de la entrada estandar y las
compare, escribiendo una cadena por pantalla que indique si son iguales o no. 
-}

ejercicioB :: IO()
ejercicioB = do
			print ("Escriba la primera linea a comparar")
			linea1 <- getLine 
			print ("Escriba la segunda linea a comparar")
			linea2 <- getLine
			let result = comparar linea1 linea2
			if result then print ("Cadenas iguales") else print ("Cadenas distintas")
			
comparar :: String -> String -> Bool
comparar [] [] = True
comparar [] l = False
comparar l [] = False
comparar (c:cs) (l:ls) = l == c && comparar cs ls

{-
Definir una funcion que lea el contenido de un fichero de texto, lo procese
invirtiendo todo el contenido y lo escriba de nuevo sobre el mismo fichero de
entrada. 
-}

ejercicioC :: IO()
ejercicioC = do
			print ("Escriba url del fichero de entrada")
			ficheroIn <- getLine
			print ("Escriba url fichero de salida") 
			ficheroOut <- getLine
			invertir <- readFile ficheroIn
			let result = invertirFichero invertir
			writeFile ficheroOut result
			print ("Fichero invertido")
			
invertirFichero :: String -> String
invertirFichero [] = []
invertirFichero fichero = foldr (\x acum -> acum ++ [x]) [] fichero

{-
Definir una funcion que sea capaz de ir leyendo líneas de la entrada estandar y las
va imprimiendo junto con el número de caracteres que tienen. Se ira ejecutando
mientras no se encuentra una línea vacía. 
-}

ejercicioD :: IO()
ejercicioD = do
			print("Introduzca una linea")
			linea <- getLine
			if linea == [] then return()
				else do
					print ("La linea " ++ linea ++ " tiene "++ show(length(linea)) ++ " caracteres" ) 
					ejercicioD
			
	
-- Definir una funcion que sea capaz de copiar el contenido de un fichero en otro. 

ejercicioE :: IO()
ejercicioE = do
				print("Escriba la url del primer fichero")
				fichero1 <- getLine
				print("Escriba la url del segundo fichero")
				fichero2 <- getLine
				--appendFile fichero1 fichero2
				contenido <- readFile fichero1
				writeFile fichero2 contenido
			