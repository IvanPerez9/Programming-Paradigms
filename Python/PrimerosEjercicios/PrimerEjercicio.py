

# Area de un rectangulo

a = 3
b= 4
area = a * b 
print("El area del rectagulo es: " , area)

# Perimetro de la circunfenecia

radio = 5
longitud = 2*3.1416 * radio 

print ("La longitud es: " , longitud)

# Precedencia, la que mas la potencia y la que menos el or 

#Si un anno es bisiesto

anno = 2000

if ((anno % 4 ==0) and not (anno & 100 == 0)) or (anno % 400 == 0) :
    print("Es bisiesto")
else:
    print("No es bisiesto")
    
    
print(3/2)
# Triangulo de N filas

n = int (input("Introduce le numero de files del triangulo: "))

for i in range(n+1):
    espacios = n -i 
    print(' ' *espacios + '*' *(2*i+1))  #Truco dejar los espacios en blanco
    
#Triangulo al reves -> dar la vuelta al rango range (n ,0 , -1)

n = int (input("Introduce le numero de files del triangulo: "))

for i in range(n-1,-1,-1):
    print(' '*(n-i) + '*' *(2*i+1))
    

