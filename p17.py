fruits = ["apple", "banana", "cherry"]
# List indexing and slicing

print(fruits[0]) # Accessing first element
print(fruits[1]) # Accessing second element
print(fruits[2]) # Accessing third element
#print(fruits[4]) # Accessing fourth element (IndexError)
print(fruits[-1]) # Accessing last element
print(fruits[-2]) # Accessing second last element

print(fruits[0:3]) # Accessing elements from index 0 to 2
print(fruits[::2]) # Accessing elements with step 2
print(fruits[::-1]) # Reversing the list

for fruit in fruits:
    print(fruit) # Iterating through the list
    
print(dir(fruits)) # List of all attributes and methods of list
print(help(fruits))# Detailed help on list methods
print(len(fruits)) # Length of the list
print("pineapple" in fruits) # Check if 'pineapple' is in the list

fruits[4] = "mango" # Modifying first element
fruits.append("coconut") # Adding an element at the end
fruits.insert(2, "orange") # Inserting an element at index 1
fruits.remove("banana") # Removing an element by value
fruits.reverse() # Reversing the list
fruits.sort() # Sorting the list
fruits.clear() # Clearing the list
fruits.index("cherry") # Finding index of an element
fruits.count("apple") # Counting occurrences of an element

# Sets

my_set = {"apple", "banana", "cherry"}
print(my_set) # Printing the set
print(dir(my_set)) # List of all attributes and methods of set
print(help(my_set))# Detailed help on set methods
print(len(my_set)) # Length of the set
print("banana" in my_set) # Check if 'banana' is in the set

print.add("orange") # Adding an element to the set
print.remove("apple") # Removing an element from the set
my_set.pop() # Removing and returning an arbitrary element
my_set.clear() # Clearing the set

#Tuples
my_tuple = ("apple", "banana", "cherry")
print(dir(my_tuple)) # List of all attributes and methods of tuple
print(help(my_tuple))# Detailed help on tuple methods
print(len(my_tuple)) # Length of the tuple
print("cherry" in my_tuple) # Check if 'cherry' is in the tuple

fruits.index("banana") # Finding index of an element
fruits.count("apple") # Counting occurrences of an element
 
for fruit in my_tuple:
    print(fruit) # Iterating through the tuple