module HojasEjercicios.HojaEjerciciosRepasoES where

{-
Función que dado un listado de nombres lo muestre por pantalla en forma de tabla.
> escribeTabla ["pepe","caramelo","lluvia"]
1: pepe
2: caramelo
3: lluvia
-}

escribeTabla :: [String] -> IO ()
escribeTabla (x:xs) =   do
						putStrLn (show n ++ ":" ++ x)
						escribeTabla xs where n =1