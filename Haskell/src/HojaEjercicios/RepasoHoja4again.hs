module HojaEjercicios.RepasoHoja4 where

--  Se quiere ordenar los elementos de una lista (cuyos elementos son comparables) mediante el algoritmo del quicksort.

quicksort ::(Ord a) => [a] -> [a]
quicksort [] = []
quicksort (c:cs) = quicksort[x | x <- cs , x < c] ++ [c] ++ quicksort[y | y <- cs , y>=c]

{-
Ejercicio B
Se pide implementar una funcion que dado un numero (de cualquier tipo que
soporte la operacion de division) y una lista de numeros del mismo tipo,
divida a ese numero por cada uno de los elementos contenidos en la lista y
devuelva una lista con el resultado.
-}

ejercicioB ::(Integral a) => [a] -> a -> [a]
ejercicioB [] _ = []
ejercicioB lista num = map ( num `div` ) lista

{-
Dado un nuevo tipo de datos para representar un árbol binario de cualquier tipo, definido
como sigue:
data Arbol a = AV | Rama (Arbol a) a (Arbol a)
Se pide definir una función que visualice el árbol por pantalla de una determinada forma:
separando cada hijo izquierdo y derecho por “|”, la raíz entre guiones y cada nivel diferente
del árbol por “( )”.

 mostrarArbol (Rama AV 5 (Rama AV 4 AV))
"()|-5-|(4)"
-}

data Arbol a = AV | Rama (Arbol a) a (Arbol a)

mostrarArbol ::(Show a) => Arbol a -> String
mostrarArbol AV = "Vacio"
mostrarArbol (Rama AV r AV) = "-" ++ show r ++ "-"
mostrarArbol (Rama izq r der) = "( |" ++ mostrarArbol izq ++ "-" ++ show r ++ "-" ++ mostrarArbol der ++ "| )"

-- D Se pide definir una función que calcule el espejo de un árbol. 

espejoArbol :: Arbol a -> Arbol a
espejoArbol AV = AV
espejoArbol (Rama AV r AV) = (Rama AV r AV)
espejoArbol (Rama izq r der) = (Rama (espejoArbol izq) r (espejoArbol der))

{- Ejercicio I 
Se pide crear una nueva CLASE de tipos, llamada Coleccion, para representar
colecciones de datos de cualquier tipo, donde los tipos pertenecientes a
esta clase tendrán el siguiente comportamiento:

	esVacia: función para saber si la colección está vacía.
	insertar: insertará un nuevo elemento en la colección.
	primero: devolverá el primer elemento de la colección.
	eliminar: eliminará un elemento de la colección.
	size: devolverá el número de elementos de la colección.
	
Algunas de las funciones anteriores variarán su implementación en función
del tipo de colección particular que sea instancia de la clase Coleccion. Por
ello, se pide crear dos instancias diferentes de esta clase para los dos
nuevos tipos de datos que se presentan a continuación:
data Pila a = Pil [a] deriving Show
data Cola a = Col [a] deriving Show
-}

data Pila a = Pil [a] deriving Show
data Cola a = Col [a] deriving Show

class Collection c where 
			esVacia :: c a -> Bool
			insertar :: c a -> a -> c a 
			primero :: c a -> a 
			eliminar :: c a -> c a
			size :: c a -> Int

instance Collection Pila where
			esVacia (Pil a) = length a == 0
			insertar (Pil a) t = Pil (a ++ [t])
			primero (Pil a) = last a
			eliminar (Pil a) = Pil (init a)
			size (Pil a) = length a
			
instance Collection Cola where
			esVacia (Col a) = length a == 0
			insertar (Col a) t = Col (a ++ [t])
			primero (Col a) = head a
			eliminar (Col a) = Col(tail a)
			size (Col a) = length a
			
{-
e) Se quiere poder mostrar por pantalla los datos de los estudiantes matriculados en una
universidad que pertenezcan a alguna de las asociaciones de esta (culturales, deportivas,
de representacion estudiantil, etc.). Para ello se deberan crear nuevos tipos de datos que
representen:
 Estudiante, de cada uno se debe disponer del nombre y titulacion
 Titulacion, que pueden ser tres: Grado II, Grado II ADE, Grado ADE
 Lista de estudiantes matriculados
 Lista de estudiantes que pertenecen a asociaciones
Un ejemplo de aplicacion de la funcion que se pide podria ser:

> mostrarAlumnosAsociaciones(listaMatriculados,listaAsociaciones)
"(Carlos Calle,GradoADE_II)(Irene Plaza,GradoADE)"

-}

data Titulacion = Grado_II | Grado_II_ADE | Grado_ADE deriving Show

data Alumno = A (String,Titulacion) deriving Show
type EstudiantesMatriculados = [Alumno]

data Asociaciones = Culturales | Deportivas | Estudiantil deriving Show
data AsociacionAlumno = AA (String, Asociaciones) deriving Show


type ListaAsociaciones = [AsociacionAlumno] 


listaAlumnos :: EstudiantesMatriculados
listaAlumnos = [ A ("Pepe" , Grado_II) , A ("Dani" , Grado_II_ADE)]

asociacionesAlumnos :: ListaAsociaciones 
asociacionesAlumnos = [AA ("Dani" ,Culturales) , AA ("Carl" ,Deportivas)]

{-
> mostrarAlumnosAsociaciones(listaMatriculados,listaAsociaciones)
"(Carlos Calle,GradoADE_II)(Irene Plaza,GradoADE)"
-}

mostrarAlumnosAsociaciones :: EstudiantesMatriculados -> ListaAsociaciones -> String
mostrarAlumnosAsociaciones [] _ = " "
mostrarAlumnosAsociaciones _ [] = " "
mostrarAlumnosAsociaciones (A (n,g):xs) (AA (n2,a):ys) = if n == n2 then n else show (mostrarAlumnosAsociaciones xs ys)

{-
type Nombre = String

    data Titulacion = GradoII | GradoADE_II | GradoADE deriving Show
    type Estudiante = (Nombre, Titulacion)

    listaEstudiantes:: [Estudiante]
    listaEstudiantes = [("Carlos", GradoII), ("Pepe Jeje", GradoADE), 
                        ("Pepe Jiji", GradoADE_II),
                        ("Pepe Jojo", GradoII), ("Pepe Juju", GradoADE_II)] 

    listaEstudiantesEnAso:: [String]
    listaEstudiantesEnAso = ["Carlos", "Pepe Jiji"]

    ej4E:: ([Estudiante], [String]) -> String 
    ej4E ([], _) = ""
    ej4E (_, []) = ""
    ej4E (((x, y):xs), (u:us)) = if (x /= u) then ej4E (xs, (u:us)) else "("++x++","++show y++")"++ej4E (xs, us)
-}

{- Ejercicio F
Se quiere poder representar una fecha de la siguiente forma: dd/mm/aaaa, para ello se
deberá crear un nuevo tipo de datos en Haskell. Por ejemplo, si se crea un nuevo tipo de
datos cuyo constructor de datos es Fecha, en el intérprete al poner fechas concretas nos
devolvería la representación de la fecha que hayamos definido:

 Fecha 10 10 2013 
 10/10/2013 
-}

type Dia = Int
type Mes = Int
type Anno = Int
data FechaTotal = Fecha Dia Mes Anno 

instance Show FechaTotal where
		show (Fecha dia mes anno) = show dia ++ "/" ++ show mes ++ "/" ++ show anno 
		
fecha :: Dia -> Mes -> Anno -> FechaTotal
fecha dia mes anno = Fecha dia mes anno

