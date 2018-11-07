module HojasEjercicios.Excepciones where

import System.IO.Error
import qualified Contol.Exception as E

handler :: IOError -> IO()
handler e = putStr "Hay problemas" 

showFile :: IO()
showFile = do
		putStr "File name" 
		name <- getLine
		contents <- readFile name
		print contents
		
main = E.catch showFile handler