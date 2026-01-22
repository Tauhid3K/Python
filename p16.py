rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

# loop inside loop
for y in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()  # New line after each inner loop iteration