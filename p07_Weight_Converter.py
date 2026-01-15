weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == 'K' or unit == 'k':
    weight = weight * 2.205
    unit = 'Lbs.'
elif unit == 'L' or unit == 'l':
    weight = weight / 2.205
    unit = 'kgs.'
else:
    print(f"{unit} was not valid")
    
print(f"Your weight is {weight} {unit}")