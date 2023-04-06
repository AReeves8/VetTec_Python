# IMPORTING PYTHON FILES

# this allows you to split your program up, into multiple files
# usually, you'll have 1 file with a specific theme of functions
# you have a "main" program, that imports those other files and functions


# import is used to import python modules
# a python module is any .py file
import math             # this imports the math library
result = math.sqrt(9)
print(result)

# to import your own files, you simply import them
#import functions                   # this imports functions.py that is in the same directory
#import Day3_examples.lists         # this imports lists.py from Day3_examples


# !!! make sure that any files you try to import are in a directory that contains a __init__.py file


# going inside helper_functions.py and grabbing the specified functions
from helper_functions import get_num_input, get_cosine, get_factorial

result = get_num_input()
print(result)

result = get_cosine(3.14)
print(result)

result = get_factorial(3)
print(result)