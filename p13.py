name = input("Enter your name: ")
# simple if- else 
''' if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")
'''

# While loop continue until the input
while name == "":
    print("You did not enter your name")
    name = name = input("Enter your name: ")
print(f"Hello {name}")

# While loop continue until the input
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: ")) 
print(f"You are {age} years old")

# While loop stops after input 
food = input("Enter a food you like () q to quit")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like () q to quit")
    
print("You quit the program")


# While loop with or condition
num = int(input("Enter a # between 1 and 10: "))

while num < 1 or num > 10:
    pritn(f"{num}is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")