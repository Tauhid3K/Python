#For loop

for x in range(1, 11):
    print(x)

print("Happy new year")

for y in reversed(range(1, 11)):
    print(y)
    
print("Happy new year")

for x in range(1, 11, 3):
    print(x)

credit_card = "1234-5678-9012-1234"

for x in credit_card:
    print(x)

for z in range(1, 21):
    if z == 13:
        continue
    else:
        print(z)

for z in range(1, 21):
    if z == 13:
        break
    else:
        print(z)