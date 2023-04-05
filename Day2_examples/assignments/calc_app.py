# welcoming the user into the calculator app
print("\n")
print("#-----------------------------------------------------#")
print("|                                                     |")
print("|     WELCOME TO AUSTIN'S WHOLE NUMBER CALCULATOR     |")
print("|                                                     |")
print("#-----------------------------------------------------#")
print("\n")

# creating an exit message that can be used anytime the program will be ended
exit_message = "\nThanks for using Austin's Whole Number Calculator. Goodbye!\n"

# presenting the menu to the user
print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")
print("[5] Modulus")
print("[0] Cancel")
menu_choice = input("Please select from the above options: ")

# converting the user input into a integer. if this can't be done, then the user did not input a whole number. 
try :
    num_choice = int(menu_choice)
except ValueError :
    print("Sorry! Only the numbers 0-5 are accepted as input.")

# this if-elif-else branch determines if the input was valid and what to do if it was valid
if num_choice < 0 or num_choice > 5 :               # checking for invalid user input
    print("Sorry! Only the numbers 0-5 are accepted as input.")
elif num_choice == 0 :                              # ending the program if they select 0
    print(exit_message)
else :                                              # all other options (input is 1-5)
    
    # result is set to be the exit message. this will only display if the user inputs an incorrect value for num1 or num2.
    result = exit_message
    
    num1 = input("Enter first whole number: ")
    if not num1.isdigit() :                         # if num1 is not a digit, tell the user and end program
        print("Sorry! Only whole numbers are allowed.")
    else :                                          # otherwise, ask for 2nd number
        num2 = input("Enter second whole number: ")
        if not num2.isdigit() :                     # if num2 is not a digit, tell the user and end program
            print("Sorry! Only whole numbers are allowed.")
        else :                                      # otherwise, perform selected operation with num1 and num2
            # addition
            if num_choice == 1 :
                result = int(num1) + int(num2)      
                print("num1 + num2 =")
            # subtraction
            elif num_choice == 2 :
                result = int(num1) - int(num2)
                print("num1 - num2 =")
            # multiplication
            elif num_choice == 3 :
                result = int(num1) * int(num2)
                print("num1 * num2 =")
            # division
            elif num_choice == 4 :
                # need to check for divide-by-zero errors
                try : 
                    result = int(num1) / int(num2)
                    print("num1 / num2 =")
                except ZeroDivisionError :
                    print("Sorry! 2nd number cannot be 0 for division operation.")
            # modulus
            elif num_choice == 5 :
                # need to check for divide-by-zero errors
                try : 
                    result = int(num1) % int(num2)
                    print("num1 % num2 =")
                except ZeroDivisionError :
                    print("Sorry! 2nd number cannot be 0 for modulus operation.")
                
    
    # displaying either the exit message or the result of the operation to the user
    print(result)

