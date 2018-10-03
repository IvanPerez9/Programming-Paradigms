module Fold.SeparaLetras where


-- Se le pasa un string y separa en una dupla, 1 las vocales otro las consonantes

separarLetras :: String -> (String,String)
separarLetras palabra = foldr(\letra (vocales,consonante) -> if (elem letra vocal) then (letra:vocales, consonante) else (vocales,letra:consonante))([],[]) palabra

-- Elem es como el pertenece pero generico 

vocal = ['A' , 'E' , 'I', 'O', 'U' , 'a', 'e' , 'i' , 'o', 'u']