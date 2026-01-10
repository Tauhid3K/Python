#typecasting Explicit vc Implicit

name = "Tauhid"
age = 25
gpa = 3.75
stutent = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(stutent))

age = float(age)  # Explicit typecasting from int to float
print(age)

gpa = int(gpa)   # Explicit typecasting from float to int
print(gpa)

stutent = str(stutent)  # Explicit typecasting from boolean to string
print(stutent)

age = bool(age)  # Explicit typecasting from int to boolean
print(age)

age2 = 0
age2 = bool(age2)  # Explicit typecasting from int to boolean

x = 5
y = 2.5

z = x/y  # Implicit typecasting from int to float
print(z)
