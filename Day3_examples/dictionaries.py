# DICTIONARIES

# dictionaries are similar to lists, exccpt the hold 2 pieces of data, per item. 
# 2 pieces of data: key and the value
# every item in a dictionary, is a key-value pair

# the key MUST ALWAYS be unique. its often an identifier of some kind.
# the value, can be anything

# syntax:
# <dictionary_name> = { 
#   <key1> : <value1>, 
#   <key2> : <value2>, 
#   ... 
# }


# a dictionary with people's name as the key, and their age as the value
people = {
    "Austin" : 23,
    "Bob" : 45,
    "Sue" : 83,
    "John" : 45,
    "Austin" : 102      # since key, "Austin" already exists the value at that key is overridden
}
print(people)


# you can use array notation ([]), to access the value of a specific key
austin_age = people["Austin"]
print(austin_age)               # this will print Austin's age

# alternatively, you can use the .get() function
bob_age = people.get("Bob")
print(bob_age)                  # this will print Bob's age



# .keys() - it returns all of your keys
people_keys = people.keys()
print(people_keys)

# .values() - it returns all of your values
people_values = people.values()
print(people_values)

# .items() - it returns all your keys and values
people_items = people.items()
for k, v in people_items :
    print(k + " is " + str(v) + " years old. ")


# inserting, updating, and deleting items in the dictionary

# insert - use array notation ([]) with a NEW key
name = "Jen"
age = 17

people[name] = age
print(people)

# update - use array notation ([]) with an EXISTING key
name2 = "Austin"
age2 = 30

people[name2] = age2    # if the key already exists, it will override the value
print(people)

# delete - .pop() function and pass in the KEY as a parameter
people.pop("John")
print(people)
