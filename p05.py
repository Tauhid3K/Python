# If else elif examoles
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("")
else: 
    print("You must be 18+ to sign up")
    
    
response =  input("Would you like food? (Y/N): ")
    
if response == 'Y' or response == 'y':  
    print("Have some food!")
else:
    print("No food for you!") 
    
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello, {name}!")
    
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")

# If else in boolean  
online = False

if online:
    print("You are online.")
else:
    print("You are offline.")