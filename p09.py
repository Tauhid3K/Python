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