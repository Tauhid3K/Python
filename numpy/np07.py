#Filtering

import numpy as np

ages = np.array([[18, 22, 70, 30, 17, 40, 45, 50],
                 [39, 24, 28, 32, 38, 42, 16, 80]])

teenagers = ages [ages < 18] 
# creates an array with ages less than 18
adults = ages[(ages >= 18) & (ages < 65)]
# creates an array with ages greater than or equal to 18 and less than 65
seniors = ages[ages >= 65]
# creates an array with ages greater than or equal to 65
even_ages = ages[ages % 2 == 0]
# creates an array with ages that are even numbers
odd_ages = ages[ages % 2 != 0]
# creates an array with ages that are odd numbers

print(teenagers) # prints the array of teenagers
print(adults) # prints the array of adults
print(seniors) # prints the array of seniors
print(even_ages) # prints the array of even ages
print(odd_ages) # prints the array of odd ages

adults = np.where(ages >= 18, ages, 0)
# creates an array where ages greater than or equal to 18 are kept as they are, and ages less than 18 are replaced with 0

print(adults) # prints the array of adults with ages less than 18 replaced by 0
#where caluse keeep the shpae of the original array and replaces the values based on the condition provided.
#it is slow compared to boolean indexing because it needs to create a new array with the same shape as the original array and fill it with the values based on the condition provided.