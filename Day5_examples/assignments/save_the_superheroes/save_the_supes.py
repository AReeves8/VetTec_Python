
from prompt_num_heroes import prompt_num_heroes
from prompt_hero_info import prompt_hero_info
from write_to_file import write_to_file
from json import loads, dumps


num_choice = -1             # stores the user's menu option as an integer
heroes = []                 # list that will be used to store all the heroes
exit_msg = "Thanks for using the Superhero Team Builder"    # an exit message to print when the user leaves the application

print("\n")
print("#-----------------------------------------------#")
print("|                                               |")
print("|     WELCOME TO THE SUPERHERO TEAM BUILDER     |")
print("|                                               |")
print("#-----------------------------------------------#")

while True :
    print("Would you like to start from scratch or add on to an existing team?")
    print("[1] Start from scratch")
    print("[2] Add to an existing team")
    print("[0] Cancel")
    user_input = input("Enter selection: ")

    error_message = "Sorry. That is an invalid selection. Try again."
    try :
        # attempting to convert the user input to a number
        num_choice = int(user_input)

        # checking that only a number from 0-2 was entered
        if (num_choice < 0) or (num_choice > 2) :
            print(error_message)
        else :
            break

    except ValueError:
        print(error_message)

# determining what to based on the user selection
if num_choice == 0 :
    # exiting the program with a nice message
    print(exit_msg)
elif num_choice == 1 :
    # start from scratch
    print("Ok, then we will start from the beginning.")
    
    # getting the number of heroes to add
    num_heroes = prompt_num_heroes()
    
    for i in range(num_heroes) :    
        # getting the hero's information
        hero = prompt_hero_info()

        # adding the hero to the list
        heroes.append(hero)

    # the file that we will save the heroes data to
    file_name = "C:/VetTec_Python/Day5_examples/assignments/save_the_superheroes/saved_superheroes.json"

    # converting the list of heroes into a dictionary
    json_str_heroes = dumps(heroes)

    # saving the data to the json file
    write_to_file(file_name, json_str_heroes)

    # informing the user of the save and leaving the program
    print("Your heroes have been saved to file " + file_name)
    print(exit_msg)

elif num_choice == 2:
    # add to an existing team
    print("Ok, then we will need a JSON file to load data from.")

    file_text = ""
    file_name = ""

    while True :
        file_name = input("Enter the name of the JSON file: ")
        
        # chcking if ".json" is anywhere in the fgiven file name. 
        # there are BETTER ways to ensure that the user gave a .json file
        if ".json" not in file_name :
            print("Sorry. We need a JSON file. Try again.")
        else :
            try :
                with open(file_name, 'r') as input_file :
                    file_text = input_file.read()

                print("Reading in file data...")
                break
            except FileNotFoundError :
                print("Sorry. The file could not be found. Try again.")

    # turning in the json file data into python data
    heroes = loads(file_text)

    # getting the number of heroes to add
    num_heroes = prompt_num_heroes()
    
    for i in range(num_heroes) :    
        # getting the hero's information
        hero = prompt_hero_info()

        # adding the hero to the list
        heroes.append(hero)

    # converting the list of heroes into a dictionary
    json_str_heroes = dumps(heroes)

    # saving the data to the json file
    write_to_file(file_name, json_str_heroes)

    # informing the user of the save and leaving the program
    print("Your heroes have been saved to file " + file_name)
    print(exit_msg)
    