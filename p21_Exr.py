import random
low = 1
high = 100

guesses = 0

number = random.randint(low, high)  # Generate random integer between low and high

print("Welcome to the Number Guessing Game!")
print("-----------------------------------")
print(f"I'm thinking of a number between {low} and {high}.")
print("Can you guess what it is?")

while True:
    guess_input = input(f"Enter a number between {low} and {high}: ") # Get user input that is in String format
    
    if guess_input.isdigit():
        guess = int(guess_input) # Convert input to integer
        guesses += 1
        
        if guess < low or guess > high:
            print("Your guess is out of range. Please try again.")
        elif guess < number :
            print(f"{guess} Too low! Try again.")
        elif guess > number:
            print(f"{guess} Too high! Try again.")
        else:
            print(f"{guess} is correct!")
            break
    else:
        print(f"Please enter a valid number between {low} and {high}.")    
    
    
print(f"You guessed the number in {guesses} attempts.")       