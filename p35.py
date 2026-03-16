#Sorting = .sort() or sorted() 
# list[], tuple(), dictonary{}, set()

fruits = ["grapes", "apple", "banana", "orange"]

fruits.sort() #sorts the list in place
print(fruits) #prints the sorted list

another_fruits = ("grapes", "apple", "banana", "orange") 
#touple cannot use .sort() method
another_fruits = sorted(fruits) #returns a new sorted tuple
print(another_fruits)           #prints the sorted tuple

another_fruits = tuple(sorted(fruits, reverse=True)) 
#converts the sorted list to a tuple
print(another_fruits) #prints the sorted tuple

new_fruits = {"grapes": 1, "apple": 2, "banana": 3, "orange": 4}

new_fruits = dict(sorted(new_fruits.items()))
#sorts the dictionary by keys and returns key and value in a new dictionary

new_fruits = dict(sorted(new_fruits.items(), key = lambda item: item[0], reverse=True))
print(new_fruits) #sorts the dictionary by keys in reverse order

new_fruits = dict(sorted(fruits.items(), key = lambda item: item[1]))
print(new_fruits) #sorts the dictionary by values

new_fruits = dict(sorted(fruits.items(), key = lambda item: item[1], reverse=True))
print(new_fruits) #sorts the dictionary by values in reverse order

#objects 

class Fruit:
    def __init__(self, name, calories): #constructor method
        self.name = name         
        self.calories = calories
        
    def __repr__(self): #string representation of the object
        return f"{self.name} ({self.calories} calories)"
        # returns the name and calories of the fruit in a string format

dict_fruits = [Fruit("grapes", 60), 
          Fruit("apple", 80), 
          Fruit("banana", 100), 
          Fruit("orange", 70)]        

dict_fruits = sorted(dict_fruits, key = lambda fruit: fruit.name)
print(dict_fruits) #sorts the list of fruit objects by name
dict_fruits = sorted(dict_fruits, key = lambda fruit: fruit.name, reverse=True)
print(dict_fruits) #sorts the list of fruit objects by name in reverse order
dict_fruits = sorted(dict_fruits, key = lambda fruit: fruit.calories)
print(dict_fruits) #sorts the list of fruit objects by calories
dict_fruits = sorted(dict_fruits, key = lambda fruit: fruit.calories, reverse=True)
print(dict_fruits) #sorts the list of fruit objects by calories in reverse order