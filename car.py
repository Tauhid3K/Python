class Car:
    def __init__(self, model, year, color, for_sale): # This is the constructor method that initializes the attributes of the Car class
        self.model = model # This attribute stores the model of the car
        self.year = year # This attribute stores the year of the car
        self.color = color # This attribute stores the color of the car
        self.for_sale = for_sale # This attribute indicates whether the car is for sale or not
        
    def drive(self): # This method simulates driving the car
        print(f"You are driving the {self.color} {self.model}.")
    
    def stop(self): # This method simulates stopping the car
        print(f"You have stopped the {self.color} {self.model}.")
    
    def describe(self): # This method provides a description of the car
        print(f"{self.year} {self.color} {self.model} - For Sale: {self.for_sale}")