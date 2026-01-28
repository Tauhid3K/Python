import random

#print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

number = random.randint(low, high)  #Generate random integer between low and high
numbers = random.random()           #Generate random float between 0.0 and 1.0
option = random.choice(options)     #Randomly select an item from a list/tuple/string
random.shuffle(cards)               #Shuffle the items in a list

print(number)
print(numbers)
print(option)
print(cards)