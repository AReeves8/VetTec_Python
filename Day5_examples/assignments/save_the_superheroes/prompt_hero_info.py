# function that prompts for name, power, and strength of the heroes that the user wants to enter
# the function takes in no parameters
# the function returns a dictionary with the heroes info
def prompt_hero_info() :
    
    print("-- NEW HERO --")
    name = input("Enter hero's name: ")
    power = input("Enter hero's super power: ")
    strength_level = input("Enter hero's strength level: ")

    # creating a dictionary with the info
    hero = {
        "name" : name,
        "power" : power,
        "strength_level" : strength_level
    }

    return hero