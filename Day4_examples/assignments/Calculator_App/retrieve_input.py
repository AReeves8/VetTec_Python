# prompts the user to input a number. if its prompting for num2, it will prevent divide-by-zero errors
# takes 2 params. the choice the user selcted and a boolean (defaulted to true) for if it is num1 or num2
# returns a valid number from the user
def retrieve_input(num_choice, is_num1 = True) :
    # while True creates an INFINITE LOOP that will ALWAYS run
    # if you do this, you HAVE to specify a break condition
    # looping until num1 is assigned a float or an int
    while True :

        # checking if we should prompt for num1 or num2
        if(is_num1) :
            num_input = input("Enter first number: ")
        else :
            num_input = input("Enter second number: ")

        # checking if the input can be converted into an int
        try :
            num = int(num_input)    

            # if its num2, ensure divide-by-zero errors don't occur
            if not is_num1 :
                if num == 0 and (num_choice == 4 or num_choice == 5) :             # if num2 is 0 and the user selected division or modulus, loop again
                    print("Sorry! Second number cannot be 0 for divison or modulus operations. Try again.")
                else :
                    break
            else :
                break
        except ValueError :
            
            # checking if the input can be converted into a float
            try :
                num = float(num_input)

                # if its num2, ensure divide-by-zero errors don't occur
                if not is_num1 :
                    if int(num) == 0 and (num_choice == 4 or num_choice == 5) :             # if num2 is 0 and the user selected division or modulus, loop again
                        print("Sorry! Second number cannot be 0 for divison or modulus operations. Try again.")
                    else :
                        break
                else :
                    break
            except ValueError :
                print("Sorry! Only numbers are allowed. Try again.")

    return num