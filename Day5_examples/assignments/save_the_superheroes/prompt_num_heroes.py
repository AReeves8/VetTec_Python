# this function prompts for the usr to enter the number of heroes they want and checks for valid data
# the function takes in no parameters
# the function returns an integer for the number of heroes to enter
def prompt_num_heroes() :
    # asking the user for input until we get valid data
    while True :
        user_input = input("How many heroes would you like to add to your team? ")

        try :
            num_heroes = int(user_input)
            break
        except ValueError :
            print("Sorry! Only whole numbers are allowed. Try again!")

    return num_heroes
