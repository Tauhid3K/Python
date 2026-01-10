item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you want to buy: "))

total = price * quantity
print(f"You have bought {quantity} X {item}")
print(f"Your total is: ${round(total, 2)}")
