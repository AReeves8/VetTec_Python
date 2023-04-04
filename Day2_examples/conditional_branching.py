# CONDITIONAL BRANCHING
# you tell python to run certain lines of code, when some condition is True

# variables to be used throughout this file
person1 = 15        # person number 1 is 15 years old
person2 = 34        # person number 2 is 34 years old
person3 = 72        # person number 3 is 72 years old
person4 = 34        # person number 4 is 34 years old


# if statements
# syntax:   if <some_condition> :
#               <some_code>
print("*** IF STATEMENTS ***")
if person3 == 15 :
    print("Person number 3 is 15 years old.")       # this code does not run since the condition is False
  #print("This indentation level will not work")
print("This is outside the if-statement")

if person2 > person1 :
    print("Person 2 is older than person 1")


# if-else statements
# syntax:   if <some_condition> :
#               <some_code>
#           else :
#               <some_other_code>
# 
# only one branch gets ran
print("*** IF-ELSE STATEMENTS ***")
if person3 < person4 :
    print("Person 3 is younger than person 4")
else :
    #print("Person 3 is older than person 4")        # not 100% - could be the same age
    print("Person 3 is at least as old as person 4")


# if-elif-else statements 
# syntax:   if <some_condition> :
#               <some_code>
#           elif <some_other_condition> :
#               <some_other_code>
#           else :
#               <some_other_other_code>
print("*** IF-ELIF-ELSE STATEMENTS ***")
if person1 > person2 :                              # can only have one - MUST BE FIRST
    print("Person 1 is older than person 2")
elif person1 == person2 :                           # can have any number of elifs - MUST BE AFTER AN IF
    print("Person 1 is the same age as person 2")
else :                                              # can have only one at the VERY END
    print("Person 1 is younger than person 2")

# remember, only one branch gets executed
if person1 > person2 :
    print("Person 1 is older than person 2")
elif person3 > person4 :
    print("Person 3 is older than person 4")    # this runs
elif person1 < person2 :
    print("Person 1 is younger than person 2")  # this does not run since the branch above it ran


if person1 > person2 :
    print("Person 1 is older than person 2")   
elif person1 < person2 :
    #print("Person 1 is younger than person 2")
    if person3 > person4 :
        print("Person 3 is older than person 4 AND person 1 is younger than person 2")


# you can use and keyword to check multiple conditions
if (person1 > person2) and (person2 > person3) :
    print("person 1 is older than person 2 AND person 2 is older than person 3")

# alternative to if-else statements
# match-case statements
# these are useful when you have specific values you want to match on
# used often with menus
# syntax:   match <variable_name> :
#               case <value1> :
#                   <some_code>
#               case <value2> :
#                   <some_code>
#               case _ :
#                   <some_default_code>
# only checks if the variable is equal to one of the case values
print("*** MATCH-CASE STATEMENTS ***")

# only available for python 3.10 or higher
num1 = 89
match num1 :
    case 10 :
        print("num1 is 10")
    case 20 :
        print("num1 is 20")
    case 30 | 40 :      
        print("num1 is either 30 or 40")
    case _ :
        print("num1 is not 10, 20, 30, or 40.")