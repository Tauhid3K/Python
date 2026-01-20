principle = 0
rate = 0
time = 0

# Different way to use while loop
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less then or equal zero")
    else:
        break
        
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less then or equal zero")     
        
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Interest rate can't be less then or equal zero")
        
total = principle * pow((1 + rate/100), time)

print(f"Balance after {time} year/s: ${total: .2f}")