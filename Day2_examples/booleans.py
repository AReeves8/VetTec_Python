# BOOLEANS AND BOOLEAN LOGIC


# booleans are special - they can only be True or False
bool1_T = True
bool2_F = False
print(type(bool1_T))


# and logic - both sides of the 'and' operator must be true, for the entire equation to be true
# if either side is false, then the entire thing is false
print("AND LOGIC TESTS:")
and_logic_test1 = bool1_T and bool2_F       # False
print(and_logic_test1)  
and_logic_test2 = bool2_F and bool1_T       # False
print(and_logic_test2)
and_logic_test3 = bool2_F and bool2_F       # False
print(and_logic_test3)
and_logic_test4 = bool1_T and bool1_T       # True
print(and_logic_test4)

# or logic - either side of the 'or' operator can be true for the entire equation to be true
# both sides have to be false for the entire thing to be false
print("OR LOGIC TESTS:")
or_logic_test1 = bool1_T or bool2_F         # True
print(or_logic_test1)  
or_logic_test2 = bool2_F or bool1_T         # True
print(or_logic_test2)
or_logic_test3 = bool2_F or bool2_F         # False
print(or_logic_test3)
or_logic_test4 = bool1_T or bool1_T         # True
print(or_logic_test4)

# not logic - will invert the bolean value that follows the 'not' operator
# so if a true statement follows a not  operator, the equation will be False
print("NOT LOGIC TESTS:")
not_logic_test1 = not bool1_T               # False
print(not_logic_test1)
not_logic_test2 = not bool2_F               # True
print(not_logic_test2)



# comparison operators
# used to compare values and gives a boolean in return

# == checks if the right and left side are equivalent, do they hold the same value?
print("== OPERATIONS")
person_age = 28
test1 = (12 == 12)              # True
print(test1)
test2 = (12 == 84)              # False
print(test2)
test3 = ((6+6) == 12)           # True
print(test3)
test4 = (person_age == 28)      # True
print(test4)

# != checks if the right and left side are NOT equivalent
print("!= OPERATIONS")
test1 = (12 != 12)              # False
print(test1)
test2 = (12 != 84)              # True
print(test2)
test3 = (person_age != 28)      # False
print(test3)

# > checks if the left side is GREATER THAN the right side
print("> OPERATIONS")
test1 = (12 > 12)               # False
print(test1)
test2 = (12 > 84)               # False
print(test2)
test3 = (84 > 12)               # True
print(test3)

# < checks if the left side is LESS THAN the right side
print("< OPERATIONS")
test1 = (12 < 12)               # False
print(test1)
test2 = (12 < 84)               # True
print(test2)
test3 = (84 < 12)               # False
print(test3)

# >= checks if the left side is GREATER THAN OR EQUAL to the right side
print(">= OPERATIONS")
test1 = (12 >= 12)              # True
print(test1)
test2 = (12 >= 84)              # False
print(test2)
test3 = (84 >= 12)              # True
print(test3)

# <= checks if the left side is LESS THAN OR EQUAL to the right side
print("<= OPERATIONS")
test1 = (12 <= 12)              # True
print(test1)
test2 = (12 <= 84)              # True
print(test2)
test3 = (84 <= 12)              # False
print(test3)

print("ADDITIONAL TESTS:")
# strings get converted into ASCII

var1 = "12"
var2 = "austin reeves"
var3 = 12
var4 = 63.23456

print((var1 == var3))           # False
print((int(var1) == var3))      # True
print((var1 < var2))            # True - because the ASCII value of "12" is less than the ASCII value of "austin reeves"

