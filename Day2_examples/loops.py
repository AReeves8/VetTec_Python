# LOOPS
# allow you to run the same code over and over again

print("*** WHILE LOOPS ***")
# while loops - run some code while some condition is true
# syntax:   while <some_condition> :
#               <some_code>

num1 = 0

while num1 < 5 :        # this will loop until num1 is greater than or equal to 5
    print(num1)
    num1 = num1 + 1
print("1st while loop is over")


# break statement - this will forcefully exit your loop
num1 = 0
while num1 < 5 :
    print(num1)

    if num1 == 3 :
        break           # this will immediately exit the loop

    num1 = num1 + 1

print("at the end of the loop, num1 = " + str(num1))



print("*** FOR LOOPS ***")
# for loops - used when you know how many times you want the loop to run
# syntax:   for <variable_name> in <value> :
#               <some code>

# this will loop 5 times
for iteration_variable in range(5) :
    print(iteration_variable)


# range() has optional parameters - start value, stop value, and a step value
# i will start at 15, go up by 2 each loop, until it reaches 30.
for i in range(15, 30, 2) :
    print(i)

# this sets the start at 50, stop at 60, and the step defaults to 1
for i in range(50, 60) :
    print(i)



# Looping until the user tells you to quit

user_input = 0          # holds the users input when asked later
print("Welcome to the times-2-inator!")

while user_input != "q" :
    user_input = input("Enter a number OR the letter q to quit: ")

    # isdigit() returns true if the string is a number
    if user_input.isdigit() :
        result = int(user_input) * 2
        print("Your number times 2 is: " + str(result))
    elif user_input == "q" :
        
        # continue will stop the current loop iteration, and go to the next iteration
        continue

        # break would work to in this use case, but break and continue are NOT the same thing
    else :
        print("Sorry! The program only allows for integers or the letter q.")