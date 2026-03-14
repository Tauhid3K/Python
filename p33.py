class Students:
    
    class_year = 2024 # This is a class variable that is shared among all instances of the Students class
    num_students = 0 # This is a class variable that keeps track of the number of students created
    
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        Students.num_students += 1 # Increment the number of students each time a new student is created
        # use the class name instade of self 
        
student1 = Students("Alice", 20)
student2 = Students("Bob", 22) 
student3 = Students("Charlie", 21)
student4 = Students("David", 23)

print(student1.name)
print(student1.age)
print(student1.class_year) # Accessing the class variable using the instance name (not recommended, but it works)

print(student2.name)
print(student2.age)
print(Students.class_year) # Accessing the class variable using the class name instead of the instance name
# This is the recommended way to access class variables

print(Students.num_students) # Accessing the class variable that keeps track of the number of students created

print(f"My graduating class of {Students.class_year} has {Students.num_students} students.") 
# Using an f-string to print the graduating class and the number of students created using the class variables
