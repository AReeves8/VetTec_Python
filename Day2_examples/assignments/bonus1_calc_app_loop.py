# welcoming the user into the calculator app
print("\n")
print("#-----------------------------------------------------#")
print("|                                                     |")
print("|     WELCOME TO AUSTIN'S WHOLE NUMBER CALCULATOR     |")
print("|                                                     |")
print("#-----------------------------------------------------#")

# creating an exit message that can be used anytime the program will be ended
exit_message = "\nThanks for using Austin's Whole Number Calculator. Goodbye!\n"

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
        
        # declaring variables to be used below
        num1 = "-1"     # making num1 a string so the loop below will run
        num2 = "-1"     # making num2 a string so the loop below will run

        # looping until num1 is assigned a whole number
        while not num1.isdigit() :
            num1 = input("Enter first whole number: ")
            if not num1.isdigit() :                                             # if num1 is not a whole number, tell the user and ask again
                print("Sorry! Only whole numbers are allowed. Try again.")
        
        # looping until num2 is assigned a whole number
        while not num2.isdigit() :
            num2 = input("Enter second whole number: ")
            if not num2.isdigit() :                                             # if num2 is not a whole number, tell the user and ask again
                print("Sorry! Only whole numbers are allowed. Try again.")
            elif int(num2) == 0 and (num_choice == 4 or num_choice == 5) :      # if num2 is 0 and the user selected division or modulus, loop again
                # asigning num2 to be a string so that the loop will run again
                num2 = "something invalid"
                print("Sorry! Second number cannot be 0 for divison or modulus operations. Try again.")
                
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
            # NOW we check to make sure 0 cannot be inserted in the loop above
            # so we don't need to check for divide-by-zero errors here
            result = int(num1) / int(num2)
            print("num1 / num2 =")
        # modulus
        elif num_choice == 5 :
            # NOW we check to make sure 0 cannot be inserted in the loop above
            # so we don't need to check for divide-by-zero errors here
            result = int(num1) % int(num2)
            print("num1 % num2 =")
              
        # displaying the result of the operation to the user
        print(result)
        

# printing the exit message before they leave the program
print(exit_message)