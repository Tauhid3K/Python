import numpy as np

array = np.array('A')

print(array.ndim)  # number of dimensions  (0D array, a scalar)

array = np.array(['A', 'B', 'C'])

print(array.ndim)  # number of dimensions (1D array)

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])

print(array.ndim)  # number of dimensions (2D array)

array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],
                  [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', ' ']]]) 
# space is used to fill the last element of the 3D array

print(array.ndim)  # number of dimensions (3D array)
print(array.shape) # shape of the 3D array (3, 3, 3) 
#-> 3 layers, each layer has 3 rows and 3 columns

array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']]])
# 3D array with shape (2 = layers, 3 = rows, 3 = columns)

print(array.ndim)  # number of dimensions (3D array)
print(array.shape) # shape of the 3D array (2, 3, 3) 

#multidimensional indexing
print(array[0])         # first layer of the 3D array 
print(array[0][0])      # first row of the first layer of the 3D array
print(array[0][0][0])   # first element of the first row of the first layer
# chained indexing = array[0][0][0] is the same as array[0, 0, 0]

array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],
                  [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', ' ']]]) 

print(array[0, 1, 0])   # first layer, second row, first column of the 3D array
print(array[0, 2, 0])   # first layer, third row, first column of the 3D array
print(array[1, 0, 0])   # second layer, first row, first column of the 3D array
print(array[2, 1, 0])   # third layer, second row, first column of the 3D array

word = array[2, 0, 0] + array[0, 1, 1] + array[2, 1, 2] + array[2, 2, 0]
print(word)  # 'WORLD' (W from array[2,1,0], O from array[0,1,1], R from array[1,2,2], L from array[2,1,2], D from array[2,2,1])