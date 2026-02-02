#Default arguments in fuictions

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(100))         # Only list_price provided, discount defaults to 0, tax defaults to 0.05
print(net_price(100, 0.1))    # list_price and discount provided, tax defaults to 0.05
print(net_price(100, 0.1, 0)) # All parameters provided

import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)  # Pause for one second between numbers
    print("Counting complete!")

count(5)  # Count from 0 to 5 (Default start value set to 0) 