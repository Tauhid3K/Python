#Exception Handle

#try:
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception:
    print("An error occurred.")
finally:
    print("This will always be executed.")
    #this use for file handle like cloasing the file after opening it
    #it will execute even if there is an error in the try block