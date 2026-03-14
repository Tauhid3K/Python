#Modules

#print(help("modules")) # Get help on modules in Python
#print(help("math"))    # Get help on the math module

import math # Import the math module
import math as m # Import the math module with an alias 'm'
from math import pi # Import only the pi constant from the math module

print(math.pi) # Access the value of pi from the math module

print(m.pi) # Access the value of pi from the math module using the alias 'm'

print(pi) # Access the value of pi from the math module using the imported constant

from math import e # Import only the e constant from the math module
print(e) # Access the value of e from the math module using the imported constant

a, b, c, d, e = 1, 2, 3, 4, 5 # Unpack values into variables a, b, c, d, e
print(e**a) # This will print the value of e raised to the power of a (which is 1)
print(e) # This will print the value of e from the math module, not the variable e defined above
print(math.e) # Access the value of e from the math module using the math module name
print(e**e) # This will print the value of e raised to the power of e (which is 5, the variable defined above)
print(math.e**e) # This will print the value of e raised to the power of e (which is 5, the variable defined above) using the math module name

import example # Import the custom module named 'example'

result = example.pi # Access the value of pi from the custom module 'example'
print(result) # Print the value of pi from the custom module
print(example.square(4)) # Call the square function from the custom module 'example' with an argument of 4
print(example.cube(3)) # Call the cube function from the custom module 'example' with an argument of 3
print(example.circumference(5)) # Call the circumference function from the custom module '
print(example.circle_area(5)) # Call the circle_area function from the custom module 'example' with an argument of 5