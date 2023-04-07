# function that presents menu to user and ensures only an int from 0-5 is returned
# takes in no parameters
# returns the selected option to the user as an integer
def print_menu() :
    
    while True :
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
            if num_choice < 0 or num_choice > 5 :               # checking for valid user input
                print("Sorry! Only the numbers 0-5 are accepted as input.")
            else : 
                break
        except ValueError :
            print("Sorry! Only the numbers 0-5 are accepted as input. Try again!")

    return num_choice