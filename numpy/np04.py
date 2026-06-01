#scalar arithmetic

import numpy as np

array = np.array([1, 2, 3])

print(array + 1) # adds 1 to each element of the array
print(array - 2) # subtracts 2 from each element of the array
print(array * 3) # multiplies each element of the array by 3
print(array / 4) # divides each element of the array by 4
print(array ** 2)# raises each element of the array to the power of 2

#vatorized math functions
print(np.sqrt(array)) # computes the square root of each element in the array

array = np.array([1.0, 2.5, 3.99])
print(np.floor(array)) # rounds down each element to the nearest integer
print(np.ceil(array))  # rounds up each element to the nearest integer
print(np.round(array)) # rounds each element to the nearest integer

print(np.pi) # prints the value of pi

redei = np.array([1, 2, 3])

print(redei * np.pi ** 2) # multiplies each element of the array by pi

#elementwise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) # adds corresponding elements of the two arrays
print(array1 - array2) # subtracts corresponding elements of the two arrays
print(array1 * array2) # multiplies corresponding elements of the two arrays
print(array1 / array2) # divides corresponding elements of the two arrays
print(array1 ** array2) # raises each element of array1 to the power of the corresponding element in array2

#comparison operators

scores = np.array([85, 90, 78, 100, 92, 88])

print(scores == 100) # checks if each score is equal to 100
print(scores != 100) # checks if each score is not equal to 100
print(scores > 60)  # checks if each score is greater than 60
print(scores < 90)  # checks if each score is less than 90
print(scores >= 60) # checks if each score is greater than or equal to 60
print(scores <= 100) # checks if each score is less than or equal to 100

scores[scores <=60] = 0 # sets all scores less than or equal to 60 to 0
print(scores) # prints the modified scores array