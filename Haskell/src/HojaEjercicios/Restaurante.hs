module HojasEjercicios.Restaurante where

import Data.Char

type MesasLibres = [Mesa]
type MesasOcupadas = [Mesa]
data Mesa = Mesa Integer Integer
data Ocupacion = O MesasLibres MesasOcupadas

instance Eq Mesa where
	Mesa iden capa == Mesa iden1 capa1 = capa == capa1
	
instance Ord Mesa where
	Mesa iden asientos >= Mesa iden2 asientos2 = asientos >= asientos2
	Mesa iden asientos <= Mesa iden2 asientos2 = asientos <= asientos2
	Mesa iden asientos > Mesa iden2 asientos2 = asientos > asientos2
	Mesa iden asientos < Mesa iden2 asientos2 = asientos < asientos2

instance Show Ocupacion where
	show (O libres ocupados) = "Las mesas libres son: " ++ show libres ++ " las ocupadas: " ++ show ocupados

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
ocuparMesaAux (O ((Mesa ident asientos):mesas) ocupadas) comensales mesasPequenas 
	| asientos >= comensales = (O (mesasPequenas ++ mesas) ((Mesa ident asientos):ocupadas))
	| otherwise = ocuparMesaAux (O mesas ocupadas) comensales (mesasPequenas ++ [(Mesa ident asientos)]) 
