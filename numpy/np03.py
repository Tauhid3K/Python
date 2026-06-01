#Slicing
import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:stop:step] [] = subscript operator
print(array[0])
#print(array[4]) 
# #IndexError: index 4 is out of bounds for axis 0 with size 4
print(array[-1]) #Negative indexing starts from the end of the array

print(array[0:2])   #Slicing from index 0 to 1 (stop index is exclusive)
print(array[1:4:2]) #Slicing from index 1 to 3 with a step of 2 
print(array[::2])   #Slicing with a step of 2 (every other row)

#Slicing columns
print(array[:,1])   #Slicing all rows and the second column (index 1)

print(array[:,1:3]) #Slicing all rows and columns from index 1 to 2 (stop index is exclusive)

#Slicing with a step of 2 for columns
print(array[:,::2]) #Slicing all rows and every other column (step of 2)

print(array[:,1::2])#Slicing all rows and columns starting from index 1 with a step of 2 (every other column starting from the second column)

print(array[:,::-2])#Slicing all rows and columns in reverse order with a step of 2 (every other column in reverse order)

#Slicing rows and columns together
print(array[0:2,0:2]) #Slicing the first two rows and the first two columns (stop index is exclusive) 

print(array[0:2, 2:]) #Slicing the first two rows and all columns starting from index 2 (stop index is exclusive for rows, but not for columns)

print(array[2:, 0:2]) #Slicing all rows starting from index 2 and the first two columns (stop index is exclusive for columns, but not for rows)

print(array[2:, 0:2]) #Slicing all rows starting from index 2 and the first two columns (stop index is exclusive for columns, but not for rows)

print(array[2:, :2])  #Slicing all rows starting from index 2 and the first two columns (stop index is exclusive for columns, but not for rows)