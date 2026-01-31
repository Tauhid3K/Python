# print("\u25CF \u250C \u2500 \u2510 \u2514 \u2518") # Unicode characters
# Output:
# ● ┌ ─ ┐ └ ┘

dice_art = {
    1: ("┌─────────┐",  # key: 1 and value as tuple
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"), # Dice face 1 in tuple format
    2: ("┌─────────┐",
        "│  ●      │",  # key: 2 and value as tuple
        "│         │",
        "│      ●  │",
        "└─────────┘"), # Dice face 2 in tuple format
    3: ("┌─────────┐",
        "│  ●      │",  # key: 3 and value as tuple
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"), # Dice face 3 in tuple format
    4: ("┌─────────┐",
        "│  ●   ●  │",  # key: 4 and value as tuple
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"), # Dice face 4 in tuple format
    5: ("┌─────────┐",
        "│  ●   ●  │",  # key: 5 and value as tuple
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"), # Dice face 5 in tuple format
    6: ("┌─────────┐",
        "│  ●   ●  │",  # key: 6 and value as tuple
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")  # Dice face 6 in tuple format
} 
# Dictionary to hold the dice faces

import random

dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll? "))

for die in range(num_of_dice):          # Roll the dice the number of times specified by the user
    dice.append(random.randint(1, 6))   # Append a random integer between 1 and 6 to the dice list 

''' # Alternative way to print the dice faces in vertical format
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)
''' 
for line in range(5):  # There are 5 lines in each dice face
    for die in dice:   # Iterate through each die rolled
        print(dice_art.get(die)[line], end = " ") # Print each line of all dice faces side by side
    print()            # New line after printing all dice for that line

for die in dice:
    total += die
print(f"You rolled a total of: {total}")
