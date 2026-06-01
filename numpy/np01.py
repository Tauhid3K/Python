import numpy as np      # import numpy library and give it an alias 'np'

print(np.__version__)   # print the version of numpy being used

my_list = [1,2,3,4]     # list

my_list = my_list * 2   # 2 times the list

print(my_list)          # [1, 2, 3, 4, 1, 2, 3, 4]

array = np.array([1,2,3,4])    # create a numpy array from the list

print(array)            # [1 2 3 4]
print(type(array))      # <class 'numpy.ndarray'>

array = array * 2      # 2 times the array
print(array)           # [2 4 6 8]