module Clases.Restaurante where

import Data.Char

{-
En un restaurante se desea gestionar las mesas libres y ocupadas de forma que 
se puedasn asignar mesas rapidamente segun llegan los comensales.

De cada mesa se necesita conocer el numero de mesas y su capacidad.
Se pide implementar un tipo de datos OCupacion (restaurante) donde se puedan saber las mesas libres y las mesas ocupadas.
LA representacion por pantalla del tipo ocupacion debe ser la siguiente.

libres : [MEsa 1 -> Capacidad: 10]
Ocupadas: [Mesa 2 -> Capacidad: 20]

Se pide:

InsertarMEsaLibre: Dada una ocupacion y una mesa, inserta la mesa en la lista de mesas libres,
de forma ordenada, con las mesas con menor capacidad primero.

OcuparMesa: Dada ocupacion y numero de comensales, esta funcion devuelve una nueva
ocupacion donde a los comensales se les ha asignado la mesa lbre mas pequeña en la que caben todos, y 
esta mesa ha sido añadida a la lista de mesas ocupadas y eliminada de la lista de 
mesas libres.
-}

type MesasLibres = [Mesa]
type MesasOcupadas = [Mesa]
data Mesa = Mesa Integer Integer
data Ocupacion = O MesasLibres MesasOcupadas

instance Eq Mesa where
	Mesa ident asientos == Mesa ident2 asientos2 = asientos == asientos2
	
instance Ord Mesa where
	Mesa ident asientos >= Mesa ident2 asientos2 = asientos >= asientos2
	Mesa ident asientos <= Mesa ident2 asientos2 = asientos <= asientos2
	Mesa ident asientos > Mesa ident2 asientos2 = asientos > asientos2
	Mesa ident asientos < Mesa ident2 asientos2 = asientos < asientos2
	
instance Show Ocupacion where
	show (O libres ocupadas) = "Libres:\n" ++ show libres ++ "\nOcupadas:\n" ++ show ocupadas
	 
instance Show Mesa where
	show (Mesa ident asientos) = "Mesa " ++ show ident ++ " -> Capacidad:" ++ show asientos
	  

addMesaLibre :: Ocupacion -> Mesa -> Ocupacion
addMesaLibre (O mesas ocupadas) mesa = O (addMesaOrdenada mesas mesa) ocupadas

addMesaOrdenada :: [Mesa] -> Mesa -> [Mesa]
addMesaOrdenada [] m = [m]
addMesaOrdenada (m1:mesas) m2
	| m1 >= m2 = m2:m1:mesas
	| otherwise = m1:addMesaOrdenada mesas m2
	
ocuparMesa :: Ocupacion -> Integer -> Ocupacion
ocuparMesa ocupacion comensales = ocuparMesaAux ocupacion comensales []


ocuparMesaAux :: Ocupacion -> Integer -> [Mesa] -> Ocupacion 
ocuparMesaAux (O (m@(Mesa ident asientos):mesas) ocupadas) comensales mesasPequenas 
	| asientos >= comensales = (O (mesasPequenas ++ mesas) (m:ocupadas))
	| otherwise = ocuparMesaAux (O mesas ocupadas) comensales (mesasPequenas ++ [m])


-- Tienes las libres y las ocupadas, vas mirando el numero de asientos en las libres que puedes meter,
-- Si no los vas pasando a un acumulador, y cuando encuentras 1, lo pasas a ocupados
-- Luego lo que te queda en libre son todas las del acumulador ++ el resto de libres 
  