# EXCEPTIONS
# exceptions are errors when you run your code
# when python knows the error that occurred




# two types of errors - syntax errors, and logic errors

# syntax errors - when you are not using correct syntax
# usually, these are easy. VS Code will tell you about these
#print("Austin Reeves"              # forgot to close parenthesis
#num 1 = 23                         # variables can't have spaces in name
#print(number1)                     # using a variable that wasn't defined


# logic errors - when your code looks right, but its wrong
# more accurately, your code does not work as intended
# often, these logic errors are the known exceptions

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

#num3 = float(num1) / float(num2)
#print("num3 = " + str(num3))



# EXCEPTION HANDLING
# use a try-except statement
try :
    num3 = float(num1) / float(num2)
    print("num3 = " + str(num3))
except ZeroDivisionError :
    print("Oops, you cannot divide by 0.")    
