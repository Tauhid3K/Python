unit = input("Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C' or unit == 'c':
    temp = round((temp * 9/5) + 32, 1)
    unit = 'F'
    print(f"The temperature is {temp}°{unit}")
elif unit == 'F' or unit == 'f':
    temp = round((temp - 32) * 5/9, 1)
    unit = 'C'
    print(f"The temperature is {temp}°{unit}")
else:
    print(f"{unit} is not valid unit")