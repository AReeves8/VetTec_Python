#import math     # this is bad practice

# this is better practice to only import the functions you need
from math import factorial, cosh

def get_num_input() :
    while True :
        user_input = input("Enter a number: ")
        try :
            int(user_input)
            break
        except ValueError :
            print("Sorry, only whole numbers allowed.")
    
    # returning the user_input as an integer
    return int(user_input)


def get_cosine(num1) :
    
    # calls the imported cosh function and return it
    return cosh(num1)


def get_factorial(num1) :

    # calls the imported factorial function and return its value
    return factorial(num1)
