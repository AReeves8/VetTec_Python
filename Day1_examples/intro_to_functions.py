# functions
# designed to take in some data, and perform some action with it

# syntax: <function_name>(<parameter1>, <parameter2>, ...)
# parameters are variables (or data) that is passed into a function
print("Austin is the best!")



# variables to be used throughout this file
num_students = 30
avg_grade = 83.24
name = "Austin Reeves"


# type() tells you the data type of the data you passed in
type(num_students)
type(2352.769)
avg_grade_type = type(avg_grade)    # whatever type() returns will be assigned to the variable
print(avg_grade_type)

print(type(name))                   # prints out what type() returns directly



# casting - the act of converting a piece of data to a NEW type

# str() - casts a piece of data to be a string
str_num_students = str(num_students)       # this converts num_students from an integer and into a string
print("The number of students in the class is " + str_num_students)
#print("The number of students in the class is " + num_students)    - gives a ValueError

print("The average grade in the class is " + str(avg_grade))

# int() - casts a piece of data to be an integer
int_avg_grade = int(avg_grade)              # converting a float to an int
print(int_avg_grade)

#int_name = int(name)                       # gives ValueError because 'Austin Reeves' is not a number
#print(int_name)

num1 = "19034"  
print(int(num1))                            # converts a string to an int

# float() - casts a piece of data to be a float
float_num_students = float(num_students)        # converts an int to a float 
print(float_num_students)

#float_name = float(name)                       # gives ValueError because 'Austin Reeves' is not a number
#print(float_name)

num1 = "19034.7293485"  
print(float(num1))                              # converts a string to a float

print(int(float(num1)))                         # converts a string to a float, then that same float to an int


# input() - takes data in from the user (opposite to print function)
print("What is your favorite color?")
#color = input()                                 # input will ALWAYS return a string
#print("Your favorite color is " + color)

#num1 = input("Enter a float: ")
#print(float(num1))


# STRING FUNCTIONS
# some functions ONLY work on certain pieces of data

# len() - takes in a string and tells you the number of characters
str_length = len(name)
print(str_length)

str_length2 = len("Austin had frito chili pie for lunch. It was tasty!")
print(str_length2)


# attribute functions - are specific to a certain piece of data
# they will only work if you already have a piece of data to work with
# syntax:   <variable_name>.<function_name>(<params>)
# dot notation is how you access an attribute of a variable

# .upper() - this converts a string into all uppercase
name_upper = name.upper()
print(name_upper)

# num_students.upper()   # won't work because num_students is not a string

# .lower() - this makes a string all lowercase
name_lower = name.lower()
print(name_lower)

# .title() - this will capitalize the first letter in every word, and lowercase the rest
name_title = name.title()
print(name_title)

# .replace(existing_phrase, new_phrase) - this will replace every instance of the existing phrase with the new one 
str1 = "Austin's favorite foods are tacos, burgers, and waffles"
new_str1 = str1.replace("tacos", "liver")
print(str1)
print(new_str1)

str2 = "Austin has 2 doggos."
str2.replace("2", "346")
print(str2)                 # doesn't modify str2