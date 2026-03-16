#iterative

def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take {step} steps")

walk(5)  

     

#recursive

def walk(steps):
    
    if steps == 0:
        return 
    walk(steps - 1) #recursive call with steps - 1
    print(f"You take {steps} steps")
    
walk(5)

# limit of recursion is 1000 by default in python

#iterative vs recursive

def factorial(x):
    result = 1
    if x > 0:
        for i in range(1, x + 1):
            result *= i
        return result

print(factorial(10))

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
   
print(factorial(10))     
# iterative = faster, complex recursive = slower, simpler 