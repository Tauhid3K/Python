price1 = 3.14159
price2 = -987.65
price3 = 12.34

# Formatted output with two decimal places
print(f"Price1: ${price1:.2f}")
print(f"Price2: ${price2:.2f}")
print(f"Price3: ${price3:.2f}")

# Formatted output with 10 character width with spaces
print(f"Price1: ${price1:10}")
print(f"Price2: ${price2:10}")
print(f"Price3: ${price3:10}")

# Formatted output with 10 character width with leading zeros
print(f"Price1: ${price1:010}")
print(f"Price2: ${price2:010}")
print(f"Price3: ${price3:010}")

# Formatted output left-aligned within 10 character width
print(f"Price1: ${price1:<10}")
print(f"Price2: ${price2:<10}")
print(f"Price3: ${price3:<10}")

# Formatted output right-aligned within 10 character width
print(f"Price1: ${price1:>10}")
print(f"Price2: ${price2:>10}")
print(f"Price3: ${price3:>10}")

# Formatted output centered within 10 character width 
print(f"Price1: ${price1:^10}")
print(f"Price2: ${price2:^10}")
print(f"Price3: ${price3:^10}")

# Formatted output with sign for positive and negative numbers
print(f"Price1: ${price1:+}")
print(f"Price2: ${price2:+}")
print(f"Price3: ${price3:+}")

# Formatted output with space for positive numbers and sign for negative numbers
print(f"Price1: ${price1: }")
print(f"Price2: ${price2: }")
print(f"Price3: ${price3: }")

# Formatted output with comma as thousand separator
print(f"Price1: ${price1:,}")
print(f"Price2: ${price2:,}")
print(f"Price3: ${price3:,}")

# Formatted output with sign and comma as thousand separator
print(f"Price1: ${price1:+,.2f}")
print(f"Price2: ${price2:+,.2f}")
print(f"Price3: ${price3:+,.2f}")