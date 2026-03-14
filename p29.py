# Variable Scope , Scope resolution = LEGB (Local, Enclosing, Global, Built-in)

import math


def func1():
    a = 10 # Local variable
    print(a)
    
def func2():
    b = 20 # Local variable
    print(b)
    
func1()
func2()

def func3():
    c = 30 # Local variable
    print(c)
    def func4():
        d = 40 # Local variable
        print(d)
        print(c) # Accessing variable c from the enclosing scope of func3
    func4() # Call func4 inside func3 to access the variable d
func3() # Call func3 to execute the code and see the scope resolution in action

def func5():
    x = 10 # Local variable
    print(x)
def func6():
    print(x)

x = 50 # Global variable

func5() # Call func5 to access the global variable x
func6() # Call func6 to access the global variable x

from math import e

def func7():
    print(e) # Accessing the built-in constant e from the math module

func7() # Call func7 to access the built-in constant e from the math module
    
e = 100 # This will create a local variable e that shadows the built-in constant e from the math module

func7() # Call func7 to access the built-in constant e from the math module
