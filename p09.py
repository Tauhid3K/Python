temp = 25
# And conditionals to check two or more conditions are true
if temp > 0 and temp <= 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")
    
temp1 = 40
# Or conditionals to check if at least one condition is true
if temp1 <= 0 or temp1 >= 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")

temp2 = 20
sunny = True
# Combined and/or conditionals

if temp2 <= 0 or temp2 >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

# Not conditional to reverse a boolean value
if not sunny:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.") 
    
#Tenary conditional operator instead of if-else for simple conditions

num = 5
print("Positive" if num > 0 else "Negative")

num1 = 6
result = "Even" if num1 % 2 == 0 else "Odd"
print(result)

a = 6
b = 7

max_num = a if a > b else b
print(f"The maximum number is {max_num}")

min_num = a if a < b else b
print(f"The minimum number is {min_num}")

age = 25

status = "Adult" if age >= 18 else "Child"
print (f"The person is an {status}.")

temp = 30
weather = "Hot" if temp > 25 else "Cold"

user_role = "Admin"

access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(f"The user has {access_level}.")

# One line shortcut of if-else statements