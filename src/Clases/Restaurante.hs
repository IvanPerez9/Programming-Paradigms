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

type NumeroMesa = Integer
type Capacidad = Integer
data Mesa = M NumeroMesa Capacidad deriving (Show,Eq,Ord)

type Libres = [Mesa]
type Ocupadas = [Mesa]
data Ocupacion = O Libres Ocupadas deriving (Show,Eq,Ord) 

insertarMesaLibre :: Ocupacion -> Mesa -> Ocupacion
insertarMesaLibre (O lib ocu) mesa = (O (lib ++ [mesa]) ocu)

ocuparMesa :: Ocupacion -> Int -> Ocupacion
ocuparMesa (O (M nmesa cap):xs ocupadas) num = if num == cap else  


-- Tienes las libres y las ocupadas, vas mirando el numero de asientos en las libres que puedes meter,
-- Si no los vas pasando a un acumulador, y cuando encuentras 1, lo pasas a ocupados
-- Luego lo que te queda en libre son todas las del acumulador ++ el resto de libres 
  