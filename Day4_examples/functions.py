# CREATING YOUR OWN FUNCTIONS

# they allow you to re-use code more easily. 


# syntax:
#   def <function_name>( <parameters> ) :
#       <some_code>
#       return <some_value>


def say_hello(name) :
    print("Hello, " + str(name))


say_hello("Brian")



def calculate_rectangle_area(length, width) :
    area = length * width
    return area


num1 = 5
num2 = 8

result = calculate_rectangle_area(num1, num2)
print(result)

print(calculate_rectangle_area(num1, num2))

# keyword syntax: assigning the variables to specific paramters
result = calculate_rectangle_area(width=num2, length=num1)



def calculate_shape_area(length, width, shape) :
    
    # making sure the shape input is always uniform
    shape = shape.lower()
    
    if shape == "rectangle" :
        return length * width
    elif shape == "triangle" :
        return (0.5) * length * width
    else :
        return None
    
result = calculate_shape_area(num1, num2, "triangle")
print(result)
result = calculate_shape_area(num1, num2, "rectangle")
print(result)

shape = input("Enter a shape: ")
result = calculate_shape_area(num1, num2, shape)
if result == None :
    print("Sorry, invlaid shape.")
else :
    print(result)


# this is a function that takes in no parameters
# it returns user input as an integer
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

num_input = get_num_input()
print(num_input)



def print_list(list_to_be_printed) :
    
    for item in list_to_be_printed :
        print(item)

fruits = ["orange", "apple", "grape"]
print_list(fruits)

# strings are just lists of characters
fruit = "banana"
print_list(fruit)

nums = [2, 3, 5]
print_list(nums)

num1 = 235
#print_list(num1)   # gives TypeError because the function is trying to iterate over an integer

num2 = 2.5
#print_list(num2)   # gives TypeError also