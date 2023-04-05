# Lists
# a single variable, that can hold multiple pieces of data

# in python, lists are sometimes referred to as arrays

# syntax:
# <list_name> = [ <item1>, <item2>, <item3>, ... ]
# the square brackets ([]) are what make it a list

fruits = ["banana", "orange", "grape", "strawberry", "lemon"]


# lists operate on indexes - that means every item in a list is associated with an index number
# the index numbers start at 0, and increase by 1 for each item in the list

# one option: you use array notation to access the index - use square brackets and the index number
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
#print(fruits[5])       # gives IndexError because fruits[5] does not exist

# you can use indexes to modify a specific value in the list
fruits[2] = "apple"
print(fruits[2])


# these are the attribute functions you'll most likely use to manipulate your list

# .append() - this will add an item to the END of the list
fruits.append("kiwi")   # now kiwi will be at the end of the list
print(fruits)           # this will print the entire list

# .insert() - will add to a list, at a specified index location
fruits.insert(3, "pineapple")   # adds pineapple to index 3, and shifts everything else back
print(fruits)

# .remove() - will delete a specific value from the list
fruits.remove("orange")         # deletes orange from the list
print(fruits)

# .pop() - will delete the value at an index location
fruits.pop(4)                   # deletes the value at index location 4
print(fruits)


# use loops to process lists
# usually use a for-loop

# "for each fruit in the list of fruits, do something"
print("*** 1st for loop ***")
for fruit in fruits :
    print(fruit)                # will print out each fruit in the list, individually

# the following for-loop does the EXACT same thing as the one above
print("*** 2nd for loop ***")
len_fruits_list = len(fruits)   # returns the number of items that are inside your list
for i in range(len_fruits_list) :
    print(fruits[i])


print("*** 3rd for loop ***")
for f in fruits :
    # adding an exclamation mark to each individual fruit
    f = f + "!"

    print(f)

# the list is not modified, only the iteration variable is modified in the loop above
print(fruits)


# you have to access the indexes to actually modify the list
print("*** 4th for loop ***")
for i in range(len(fruits)) :
    fruits[i] = fruits[i] + "!"

print(fruits)