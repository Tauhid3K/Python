fruits = ["apple", "banana", "cherry"]
vegitables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "beef", "pork"]

groceries = [fruits, vegitables, meats]


print(fruits) # Printing the list of fruits 1D
print(groceries) # Printing the list of groceries 2D
print(groceries[0]) # Accessing first element (fruits) of groceries 2D
print(groceries[0][2]) # Accessing third element (cherry) of fruits in groceries 2D

groceries01 = [["apple", "banana", "cherry"],
             ["carrot", "broccoli", "spinach"], 
             ["chicken", "beef", "pork"]] # 2D list

for collection in groceries01:
    for food in collection:
        print(food, end=", ")
    print()  # New line after each inner loop iteration

# There can be list of toules, list of sets, set of tuples, tuple of lists etc.