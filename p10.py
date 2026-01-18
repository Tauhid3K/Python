name = input("Enter your name: ")

# length of string
result =len(name)
# first occurrence
result1 = name.find("h")
# last occurrence
result2 = name.rfind("q")
# capitalize the string only first letter 
name1 = name.capitalize()
# all uppercase
name2 = name.upper()
# all lowercase
name3 = name.lower()
# check if all characters are digits
name4 = name.isdigit()
# check if all characters are alphabetic
name5 = name.isalpha()
 
print(result)
print(result1)
print(result2)
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)

phone_number = input("Enter your phone number: ")
# count occurrences of a substring
result2 = phone_number.count("-")
# replace substring with another substring
result3 = phone_number.replace("-", "")


print(result2)
print(result3)

print(help(str))