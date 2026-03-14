#POOP python object oriented programming

from car import Car # Import the Car class from the car module
        
car1 = Car("BMW", 2020, "Black", True) # Create an instance of the Car class with specific attributes
car2 = Car("Lamborghini", 2021, "Red", False) # Create another instance of the Car class with specific attributes

print(car1) # This will print the memory address of the car1 object, which is not very informative
print(car1.model) # This will print the model of the car1 object
print(car1.year) # This will print the year of the car1 object
print(car1.color) # This will print the color of the car1 object
print(car1.for_sale) # This will print whether the car1 object is for sale or not

print(car2) # This will print the memory address of the car2 object, which is not very informative
print(car2.model) # This will print the model of the car2 object
print(car2.year) # This will print the year of the car2 object
print(car2.color) # This will print the color of the car2 object
print(car2.for_sale) # This will print whether the car2 object is for sale or not

car1.drive() # Call the drive method on the car1 object to simulate driving the car
car1.stop() # Call the stop method on the car1 object to simulate stopping the car
car2.drive() # Call the drive method on the car2 object to simulate driving the car
car2.stop() # Call the stop method on the car2 object to simulate stopping the car

car1.describe() # Call the describe method on the car1 object to get a description of the car
car2.describe() # Call the describe method on the car2 object to get a description of