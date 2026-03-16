#lambda function = lambda arguments: expression

double = lambda x: x * 2 
#def double(x)
print(double(5))

add = lambda x, y: x + y
print(add(3, 4))
#def add(x, y):

max_value = lambda a, b: a if a > b else b 
print(max_value(10, 20))
#def max_value(a, b):
min_value = lambda a, b: a if a < b else b
print(min_value(10, 20))
#def min_value(a, b):

full_name = lambda first, last: first + " " + last
print(full_name("Tauhid", "Shahriar"))
#string concatenation

is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(5))
#def is_even(x):

age_check = lambda age : True if age >= 18 else False
print(age_check(20))
print(age_check(15))
#def age_check(age):