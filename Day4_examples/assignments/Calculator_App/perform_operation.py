# using numpy for mathematical operations
import numpy as np

# performs the selected mathematical operation
# takes in 3 params. user input num1 and num2, as well as the user's selected operation
# returns the result of the operation
def perform_operation(num1, num2, num_choice) :
    # addition
    if num_choice == 1 :
        result = np.add(num1, num2) 
        print("num1 + num2 =")
    # subtraction
    elif num_choice == 2 :
        result = np.subtract(num1, num2)
        print("num1 - num2 =")
    # multiplication
    elif num_choice == 3 :
        result = np.multiply(num1, num2)
        print("num1 * num2 =")
    # division
    elif num_choice == 4 :
        result = np.divide(num1, num2)
        print("num1 / num2 =")
    # modulus
    elif num_choice == 5 :
        result = np.mod(num1, num2)
        print("num1 % num2 =")
            
    # returning the result
    return result