#Positional Arguments 
def happy_birthday(name, age): # Parameters: name (str), age (int)
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to you!")
    print()
    
# Example usage:
happy_birthday("Bro", 25)   # Arguments: "Bro" (str), 25 (int)
happy_birthday("Alice", 30) # Arguments: "Alice" (str), 30 (int)
happy_birthday("Bob", 40)  # Arguments: "Bob" (str), 40 (int) 

def display_invoice(username, amount, due_date): # Parameters: username (str), amount (float), due_date (str)
    print(f"Hello {username},")
    print(f"Your bill of ${amount:.2f} is due on {due_date}.")
    
display_invoice("Tauhid", 150.75, "2026-07-15")  # Arguments: "Tauhid" (str), 150.75 (float), "2026-07-15" (str)

# Using return statements in functions
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print() 

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = first_name + " " + last_name
    return full_name

full_name = create_name("tauhid", "shahriar")
print(full_name)