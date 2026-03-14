
#iterable 
number = [1, 2, 3, 4, 5]

for item in number:
    #print(item) #this will print the numbers in the list on separate lines
    print(item, end=" ") #this will print the numbers in the list on the same line with a space in between

print() #this will print a new line after the previous print statement  
    
for i in reversed(number):
    print(i, end=" ") #this will print the numbers in the list in reverse order on the same line with a space in between

numbers = (1, 2, 3, 4, 5) #this is a tuple

for number in numbers:
    print(number, end=" ") #this will print the numbers in the tuple on the same line with a space in between

print() #this will print a new line after the previous print statement

fruits = {"apple", "banana", "cherry"} #this is a set

for fruit in fruits:
    print(fruit, end=" ") #this will print the fruits in the set on the same line with a space in between

for fruit in reversed(fruits):    
    print(fruit, end=" ") # 'set' object is not reversible
    
name = "Tauhid Shahriar"

for character in name:
    print(character, end=" ") #this will print the characters in the string on the same line with a space in between

print() #this will print a new line after the previous print statement
    
my_dict = {"A": 1, "B": 2, "C": 3}

for key in my_dict:
    print(key, end=" ") #this will print the keys in the dictionary on the same line with a space in between 
   
for value in my_dict.values():
    print(value, end=" ") #this will print the values in the dictionary on the same line with a space in between

for key, value in my_dict.items():
    print(key, value, end=" ") #this will print the keys and values in the dictionary on the same line with a space in between each key-value pair
    print(f"{key}: {value}", end=" ") #this will print the keys and values in the dictionary in a key: value format on the same line with a space in between each key-value pair