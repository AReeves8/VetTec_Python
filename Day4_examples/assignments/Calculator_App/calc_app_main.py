
from print_menu import print_menu
from retrieve_input import retrieve_input
from perform_operation import perform_operation


# welcoming the user into the calculator app
print("\n")
print("#----------------------------------------------#")
print("|                                              |")
print("|     WELCOME TO AUSTIN'S MAGIC CALCULATOR     |")
print("|                                              |")
print("#----------------------------------------------#")

# creating an exit message that can be used anytime the program will be ended
exit_message = "\nThanks for using Austin's Magic Calculator. Goodbye!\n"

#creating the variable that will store the user's input as an integer
num_choice = -1

while num_choice != 0 :
    
    num_choice = print_menu()

    # checking if the user wants to quit the app
    if num_choice > 0 :                              
        # prompting the user's for input
        num1 = retrieve_input(num_choice)
        num2 = retrieve_input(num_choice, is_num1=False)
        
        # doing the calculations
        result = perform_operation(num1, num2, num_choice)
              
        # displaying the result of the operation to the user
        print(result)
        
# printing the exit message before they leave the program
print(exit_message)


