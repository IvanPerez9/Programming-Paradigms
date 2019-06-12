import numpy as np

"""
Create a 4X2 integer array and Prints its attributes
"""

array = np.arange(8).reshape(4,2)
print(array)
print(array.shape)
print(array.ndim)
print(array.itemsize)

"""
Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
"""

array2 = np.arange(100, 200 , 10).reshape(5,2)
print(array2)


"""
Provided numPy array. return array of items in the third column from all rows
"""

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
new = sampleArray[...,2] # fila y columna
print(new)

# Se cada 2 filas, las columnas 1 y 2
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
newArray = sampleArray[::2, 1::2]
print(newArray)


"""
Dividir el array en 4 iguales
"""

print("Creating 8X3 array using numpy.arange")
sampleArray = np.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)
print("\nDividing 8X3 array into 4 sub array\n")
subArrays = np.split(sampleArray, 4)
print(subArrays)

"""
Ordenar array
"""

print("Printing Original array")
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)
sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
print("Sorting Original array by secoond row")
print(sortArrayByRow)
print("Sorting Original array by secoond column")
sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)

""" 
Maximo y minimo -> axis = 1 filas y axis = 0 columnas
"""

print("Printing Original array")
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)
minOfAxisOne = np.amin(sampleArray, 1)
print("Printing amin Of Axis 1")
print(minOfAxisOne)
maxOfAxisOne = np.amax(sampleArray, 0)
print("Printing amax Of Axis 0")
print(maxOfAxisOne)


"""
Borrado
"""

print("Printing Original array")
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print (sampleArray)
print("Array after deleting column 2 on axis 1")
sampleArray = np.delete(sampleArray , 1, axis = 1)
print (sampleArray)
arr = np.array([[10,10,10]])
print("Array after inserting column 2 on axis 1")
sampleArray = np.insert(sampleArray , 1, arr, axis = 1)
sampleArray = np.insert(sampleArray , 1, arr, axis = 1)
print (sampleArray)
