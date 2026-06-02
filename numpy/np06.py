#Aggregate functions 
#summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])

print(np.sum(array)) # sums all the elements in the array
print(np.mean(array)) # calculates the mean of all the elements in the array
print(np.std(array)) # calculates the standard deviation of all the elements in the array
print(np.var(array)) # calculates the variance of all the elements in the array

print(np.min(array)) # finds the minimum value in the array
print(np.max(array)) # finds the maximum value in the array
print(np.argmin(array)) # finds the index of the minimum value in the array
print(np.argmax(array)) # finds the index of the maximum value in the array

print(np.sum(array, axis=0)) # sums the elements in the array along the columns (axis 0)
print(np.sum(array, axis=1)) # sums the elements in the array along the rows (axis 1)