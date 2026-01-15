weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == 'K' or unit == 'k':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f"Your weight is {weight} {unit}")
elif unit == 'L' or unit == 'l':
    weight = weight / 2.205
    unit = 'kgs.'
    print(f"Your weight is {weight} {unit}")
else:
    print(f"{unit} is not valid")