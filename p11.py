credit_number = "1234-5678-9012-3456"

# Accessing characters by index
print(credit_number[5])

# Slicing the string to get substrings
print(credit_number[0:4])

# Slicing to get middle segment
print(credit_number[5:9])

# Sclicing to get last segment
print(credit_number[10:])

# Get the last fourth character
print(credit_number[-4])

# Get every fourth(n-th) character
print(credit_number[::4])

# last four digits of the credit card
last_digits = credit_number[-4:]
print(f"The last four digits of the credit card are {last_digits}.")

# Reverse the credit card number
credit_number = credit_number[::-1]
print(credit_number)