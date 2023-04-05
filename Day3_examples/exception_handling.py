# EXCEPTION HANDLING 

# allows you to catch exceptions or errors in your code before 
# your code crashes and displays that error to the user

# every try HAS TO have an except
# syntax:
# try :
#   <some_risky_code>
# except <error_name>  :
#   <some_code_to_handle_that_specific_error>
# except <error_name2>, <error_name3> :
#   <some_other_code>

# make sure you catch exceptions in order from most to least specific
try :
    print("hello")
except Exception :                      # this is the most general Exception you can catch
    print("exception caught")           # so if ANY error is thrown, this will run
except ValueError :
    print("never will be seen")         # this is unreachable

# proper order of catcing exceptions
try :
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    result = int(num1) / int(num2)      # as soon as the error happens, your code will jump to an except branch
    print(result)
except ZeroDivisionError :
    print("Woah! You can't divide by zero!")
except ValueError :
    print("Woah! You can only input numbers!")
except Exception :
    print("Woah! Something went wrong.")

# try inside of an if-statement
if (12 > 2) :
    try :
        print("hello")
    except Exception :
        print("error")

# try-except EXTRAS
# these are optional and have specific uses
try : 
    print("hello")
except Exception :
    print("error")
else :
    print("this will only run, if an exception WAS NOT thrown")
finally :
    print("this will ALWAYS run")