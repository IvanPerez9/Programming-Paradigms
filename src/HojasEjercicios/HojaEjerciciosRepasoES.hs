module HojasEjercicios.HojaEjerciciosRepasoES where

{-
Función que dado un listado de nombres lo muestre por pantalla en forma de tabla.
> escribeTabla ["pepe","caramelo","lluvia"]
1: pepe
2: caramelo
3: lluvia
-}

escribeTabla :: [String] -> IO ()
escribeTabla s =  escribeTablaAux s 1
						
escribeTablaAux :: [String] -> Int -> IO ()
escribeTablaAux [] cont = return()
escribeTablaAux (x:xs) cont = do
							  print(show cont ++ ":" ++ x)
							  escribeTablaAux xs (cont+1)
							  

{-
Definir una función que sea capaz de leer dos líneas de la entrada estándar y las
compare, escribiendo una cadena por pantalla que indique si son iguales o no.
> comparaCadenas
Introduce la primera linea: linea1
Introduce la segunda linea: hola
Las cadenas son diferentes
-}

comparaCadenas :: [String] -> [String] -> IO ()
comparaCadenas l1 l2 = compararCadenasAux l1 l2 

compararCadenasAux :: [String] -> [String] -> IO ()
compararCadenasAux [] _ = print "No son iguales" 
compararCadenasAux _ [] = print "No son iguales"
compararCadenasAux  




