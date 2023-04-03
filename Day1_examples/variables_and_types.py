
# variables are a way to hold data in a meaningful way
# syntax: <variable_name> = <some_value>
# the equal sign (=) is called the assignment operator
num1 = 12

# this will print out the value that is inside num1
print(num1)

# naming convention - industry standard for how to name variables
# python's naming convention is to use underscores for spaces
days_in_a_week = 7
print(days_in_a_week)


# data types - python has many but int, float, string, boolean are the big ones
num1 = 3                        # integer (int) - any whole number
weeks_in_a_year = 52.143        # float - a number with a decimal 
user_name = "Austin Reeves"     # string - any text
user_name2 = 'Austin Reeves2'   # strings can also be created with single quotes

# string concatenation - uses the plus sign to append one string to another
new_string = user_name + " " + user_name2
print(new_string)

# variables can be overridden - now this will print 3
# overriding variable names that you're STILL using is bad practice
# better to just use a new variable
num1 = "Austin likes tacos."
print(num1)


# BEST PRACTICE to use decriptive variables names
# that way you know what your code is doing
num_days_in_year = days_in_a_week * weeks_in_a_year
print(num_days_in_year)



# Arithmetic Operators - how to do math

num1 = 8
num2 = 5


# addition - plus sign (+)
add_result = num1 + num2
print(add_result)

# subtraction - minus sign or hyphen or dash (-)
sub_result = num1 - num2
print(sub_result)

neg_result = num2 - num1
print(neg_result)

# multiplication - asterisk (*)
mul_result = num1 * num2
print(mul_result)

# division - forward slash (/)
div_result = num1 / num2
print(div_result)

#bad_result = num1 / 0
ok_result = 0 / num1
print(ok_result)

# modulus - precent sign (%)
# returns the remainder from a division operation
mod_result = num1 % num2
# 8 / 5 = 1.6 and then .6 * 5 = mod_result
print(mod_result)