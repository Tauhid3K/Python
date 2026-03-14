# Membership Operators: in, not in
word = "APPLE"

letter = input("Guess a letter: ").upper()

if letter in word:
    print("Correct!")
else:
    print("Incorrect!")

''' Alternative way to write the above code (Complex way)     
if letter not in word:
    print("Incorrect!")
else:
    print("Correct!")
'''

students = {"Alice", "Bob", "Charlie"}

student = input("Enter a student's name: ").capitalize()

if student in students:
    print(f"{student} is a student.")   
else:
    print(f"{student} is not a student.")
    
'''
Alternative way to write the above code (Complex way)
if student not in students:
    print(f"{student} is not a student.")  
else:
    print(f"{student} is a student.")
'''

grade = {"Sandy": "A", "Tom": "B", "Jerry": "C", "Mickey": "D", "Donald": "F"}

student = input("Enter a student's name: ").capitalize()

if student in grade:
    print(f"{student}'s grade is {grade[student]}.")
else:
    print(f"{student} is not a student.")
    
email = input

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")