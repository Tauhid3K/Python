# Concession Stand Menu Program
menu = {"pizza": 3.00,
        "pasta": 2.50,
        "salad": 1.50,
        "soda": 1.00,
        "dessert": 2.00,
        "coffee": 1.25,
        "tea": 1.00,
        "sandwich": 2.75,
        "soup": 2.00,
        "bread": 1.00}

cart = [] # list to store items added to the cart
total = 0 # variable to store the total cost

print("-------Menu-------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None: # Check if the item exists in the menu
        cart.append(food)
print()

print('-------Your Order-------')    # Print the items in the cart and calculate the total cost
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f'Total is : ${total:.2f}')    # Print the total cost
print('------------------------')