#Keyword arguments in functions

def hello(gretting, title, first, last):
    print(f"{gretting}, {title} {first} {last}!")
    
hello(gretting="Hello", title="Mr.", first="Tauhid", last="Shahriar") # Using keyword arguments
hello(first="Alice", last="Smith", gretting="Hi", title="Dr.")        # Different order with keyword arguments
hello("Hello" , title="Ms.", first="Eva", last="Brown")               # Mixing positional and keyword arguments 
                                                                      #(Positional Argument always first)

for x in range(1, 11):
    print(x, end=" ")           # end is the keyword argument here
print()

print("1","2","3","4", sep="-") # sep is the keyword argument here

def get_phone(country, area, first, last):
    return f"+{country} ({area}) {first}-{last}"

phone_num = get_phone(area= 555, country=1, first=123, last=4567) # Using keyword arguments
print(phone_num)