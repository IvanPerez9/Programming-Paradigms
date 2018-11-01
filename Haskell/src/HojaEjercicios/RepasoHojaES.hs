module HojaEjercicios.RepasoHojaES where

{-
Funcion que dado un listado de nombres lo muestre por pantalla en forma de tabla.
> escribeTabla ["pepe","caramelo","lluvia"]
1: pepe
2: caramelo
3: lluvia
-}

ejercicioA :: [String] -> IO()
ejercicioA listaN = ejercicioAaux listaN 1 

ejercicioAaux :: [String] -> Int -> IO ()
ejercicioAaux [] contador = return()
ejercicioAaux (l:ls) contador = do
								print (show contador ++ "." ++ l)
								ejercicioAaux ls (contador+1) 
								


{-
Definir una funcion que sea capaz de leer dos lineas de la entrada estandar y las
compare, escribiendo una cadena por pantalla que indique si son iguales o no. 
-}

ejercicioB :: IO ()
ejercicioB = do
				print ("Escribe la primera linea")
				linea1 <- getLine
				print ("Escribe la segunda linea")
				linea2 <- getLine
				let result = compararCadenas linea1 linea2
				if result then print ("Cadenas iguales") else print ("Cadenas distintas")
			
compararCadenas :: String -> String -> Bool
compararCadenas [ ] [ ] = True
compararCadenas [] _ = False
compararCadenas _ [] = False
compararCadenas (l:ls) (x:xs) = (l == x) && (compararCadenas ls xs )

{-
Definir una funcion que lea el contenido de un fichero de texto, lo procese
invirtiendo todo el contenido y lo escriba de nuevo sobre el mismo fichero de
entrada. 
-}

ejercicioC :: IO()
ejercicioC = do
				print ("Introduzca la ruta del fichero a leer")
				archivoLeer <- getLine
				print ("Introduzca la ruta del archivo a escribir")
				archivoEscribir <- getLine
				fileR <- readFile archivoLeer
				let result = invertir fileR
				writeFile archivoEscribir result
				
invertir :: [a] -> [a]
invertir lista = foldr (\x acum -> acum ++ [x]) [] lista

{-
Definir una funcion que sea capaz de ir leyendo líneas de la entrada estandar y las
va imprimiendo junto con el número de caracteres que tienen. Se ira ejecutando
mientras no se encuentra una línea vacía. 
-}

ejercicioD :: IO()
ejercicioD = do
			print ("Introduce linea")
			linea <- getLine
			if linea == [] then return() -- Hace que pare si linea vacia
				else do
					print ("Tiene:" ++ (show(length linea)) ++ " caracteres" )
					ejercicioD
			


-- Definir una funcion que sea capaz de copiar el contenido de un fichero en otro. 

ejercicioE :: IO()
ejercicioE = do
				print ("Introduce el primer fichero")
				file1 <- getLine
				print ("Introduce el segundo fichero")
				file2 <- getLine
				contenido <- readFile file1
				writeFile file2 contenido
				