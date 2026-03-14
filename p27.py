# list comprehensions [Expression for value in iterable if condition]
doubles = []

for i in range(1, 11):
    doubles.append(i * 2)

print(doubles, end=" ") # this will print the list of doubles on the same line with a space in between each number

print() # this will print a new line after the previous print statement

doubles = [i*2 for i in range(1, 11)] # this is a list comprehension that creates a list of doubles from 1 to 10
print(doubles, end=" ") # this will print the list of doubles on the same line with a space in between each number

print() # this will print a new line after the previous print statement

triples = [j*3 for j in range(1, 11)] # this is a list comprehension that creates a list of triples from 1 to 10
print(triples, end=" ") # this will print the list of triples on the same line with a space in between each number

print() # this will print a new line after the previous print statement

squares = [k*k for k in range(1, 11)] # this is a list comprehension that creates a list of squares from 1 to 10
print(squares, end=" ") # this will print the list of squares on the same line

print() # this will print a new line after the previous print statement

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits = [fruit.upper() for fruit in fruits] # this is a list comprehension that creates a new list of fruits in uppercase
print(fruits, end=" ") # this will print the list of fruits in uppercase on the

print() # this will print a new line after the previous print statement

fruit_char = [fruit[0] for fruit in fruits] # this is a list comprehension that creates a new list of the first character of each fruit
print(fruit_char, end=" ") # this will print the list of the first character of each fruit on the same line with a space in between each character

print() # this will print a new line after the previous print statement

numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_nums = [num for num in numbers if num > 0] # this is a list comprehension that creates a new list of only the positive numbers from the original list
print(positive_nums, end=" ") # this will print the list of positive numbers on the same line with a space in between each number

print() # this will print a new line after the previous print statement

negative_nums = [num for num in numbers if num < 0] # this is a list comprehension that creates a new list of only the negative numbers from the original list
print(negative_nums, end=" ") # this will print the list of negative numbers on the same line with a space in between each number

print() # this will print a new line after the previous print statement

even_nums = [num for num in numbers if num % 2 == 0] # this is a list comprehension that creates a new list of only the even numbers from the original list
print(even_nums, end=" ") # this will print the list of even numbers on the same line with a space in between each number

odd_nums = [num for num in numbers if num % 2 != 0] # this is a list comprehension that creates a new list of only the odd numbers from the original list
print(odd_nums, end=" ") # this will print the list of odd numbers on the same line with a space in between each number

print() # this will print a new line after the previous print statement

grades = [85, 92, 78, 90, 88, 56, 61, 95, 82, 70]

passing_grades = [grade for grade in grades if grade >= 60] # this is a list comprehension that creates a new list of only the passing grades from the original list
print(passing_grades, end=" ") # this will print the list of passing grades on  
