import math

# Circle calculations
radious = float(input('Enter the radious of the circle: '))

circumference = 2 * math.pi * radious

print(f'THe circumference of the circle is: {round(circumference, 2)}cm')

area = math.pi * radious**2

print(f'The area of the circle is: {round(area, 2)}cm^2')

# Hypotenuse calculation
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))

c = pow(a, 2) + pow(b, 2)

result = math.sqrt(c)

print(f'The hypotenuse is: {round(result, 2)}cm')
