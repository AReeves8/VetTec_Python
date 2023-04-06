print("\n")
print("#-----------------------------------------------#")
print("|                                               |")
print("|     WELCOME TO THE SUPERHERO TEAM BUILDER     |")
print("|                                               |")
print("#-----------------------------------------------#")


while True :

    # creating the list we will use to store the heroes
    heroes = []

    # asking the user for input until we get valid data
    while True :
        num_heroes = input("How many heroes would you like to add to your team? ")

        try :
            int(num_heroes)
            break
        except ValueError :
            print("Sorry! Only whole numbers are allowed. Try again!")

    # getting te hero information
    for i in range(int(num_heroes)) :
        name = input("Enter hero " + str(i+1) + "'s name: ")
        power = input("Enter hero " + str(i+1) + "'s super power: ")
        strength_level = input("Enter hero " + str(i+1) + "'s strength level: ")

        # creating a dictionary with the info
        hero = {
            "name" : name,
            "power" : power,
            "strength_level" : strength_level
        }

        # adding the hero to the list
        heroes.append(hero)

    # looping through the list of heroes
    for hero in heroes :
        
        # accessing the individual keys to print out the heroes info
        print(str(hero.get("name")) + " has a super power of " + str(hero.get("power")) + " and a strengh level of " + str(hero.get("strength_level")) + ".")

    user_input = input("Would you like to build another team? (Y/N)")
    if user_input == "N" :
        break

