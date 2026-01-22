# Shoping cart sprogram

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (or 'q' to quit): ")
    if food.lower() == 'q': # Convert to lowercase to handle 'Q' as well
        break
    else:
        price = float(input(f"Enter price for {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("---- Your Shopping Cart ----")
for food in foods:
    print(food, end=", ") # Print all food items with comma separation    
    
for price in prices:
    total += price  # Calculate total price
    
print(f"\nTotal price: ${total: .2f}")