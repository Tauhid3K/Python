#Broadcasting
import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape) # prints the shape of array1
print(array2.shape) # prints the shape of array2
# Rule is it requires the columns of array1 and 
# the columns of array2 needs to be the same or one of them needs to be 1
# the rows of array1 and the rows of array2 needs to be the same or one of them needs to be 1

print(array1 * array2) # multiplies array1 and array2 using broadcasting

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[1], [2]])

print(array1.shape) # prints the shape of array1
print(array2.shape) # prints the shape of array2

print(array1 * array2) # multiplies array1 and array2 using broadcasting

array1 = np.array([[1, 2], [3, 4], [5, 6]])
array2 = np.array([[1, 2, 3], [4, 5, 6]])

print(array1.shape) # prints the shape of array1
print(array2.shape) # prints the shape of array2

# This will raise an error because the shapes of the arrays are not compatible for broadcasting
# columns of array1 (2) does not match columns of array2 (3) and 
# rows of array1 (3) does not match rows of array2 (2)
# print(array1 * array2) # this will raise an error