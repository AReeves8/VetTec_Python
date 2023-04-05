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
    # presenting the menu to the user
    print("\n")
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
        print("Sorry! Only the numbers 0-5 are accepted as input. Try again!")
        
        # moving on to next loop so they can input a valid menu choice and skip over everything else in the current iteration
        continue        

    # this if-elif-else branch determines if the input was valid and what to do if it was valid
    if num_choice < 0 or num_choice > 5 :               # checking for valid user input
        print("Sorry! Only the numbers 0-5 are accepted as input.")
    elif num_choice == 0 :                              # exiting the loop and ending the program if they select 0
        break
    else :                                              # all other options (input is 1-5)
        
        # while True creates an INFINITE LOOP that will ALWAYS run
        # if you do this, you HAVE to specify a break condition
        # looping until num1 is assigned a float or an int
        while True :
            num1_input = input("Enter first number: ")

            try :
                num1 = int(num1_input)
                break
            except ValueError :
                try :
                    num1 = float(num1_input)
                    break
                except ValueError :
                    print("Sorry! Only numbers are allowed. Try again.")
        
        # looping until num2 is assigned a float or an int
        while True :
            num2_input = input("Enter second number: ")

            try :
                num2 = int(num2_input)

                if num2 == 0 and (num_choice == 4 or num_choice == 5) :             # if num2 is 0 and the user selected division or modulus, loop again
                    print("Sorry! Second number cannot be 0 for divison or modulus operations. Try again.")
                else :
                    break
            except ValueError :
                try :
                    num2 = float(num2_input)

                    if int(num2) == 0 and (num_choice == 4 or num_choice == 5) :      # if num2 is 0 and the user selected division or modulus, loop again
                        print("Sorry! Second number cannot be 0 for divison or modulus operations. Try again.")
                    else :
                        break
                except ValueError :
                    print("Sorry! Only numbers are allowed. Try again.")
                
        # addition
        if num_choice == 1 :
            result = num1 + num2 
            print("num1 + num2 =")
        # subtraction
        elif num_choice == 2 :
            result = num1 - num2
            print("num1 - num2 =")
        # multiplication
        elif num_choice == 3 :
            result = num1 * num2
            print("num1 * num2 =")
        # division
        elif num_choice == 4 :
            # NOW we check to make sure 0 cannot be inserted in the loop above
            # so we don't need to check for divide-by-zero errors here
            result = num1 / num2
            print("num1 / num2 =")
        # modulus
        elif num_choice == 5 :
            # NOW we check to make sure 0 cannot be inserted in the loop above
            # so we don't need to check for divide-by-zero errors here
            result = num1 % num2
            print("num1 % num2 =")
              
        # displaying the result of the operation to the user
        print(result)

# printing the exit message before they leave the program
print(exit_message)