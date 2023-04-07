
# importing the loads and dumps functions from the JSON module
from json import loads, dumps


# FILE I/O - file input and output

# being able to read and write data to and from a file


# open() - opens up a file to be used in code
# takes in 2 parameters: 
#       file path to a specific file
#       file operation to perform
#           do you want to read from the file (r), 
#           write to the file (w), 
#           append to a file (a), 
#           or create the file (x)

# this is the relative path, meaning relative to the folders the current project is in
file_path = "Day5_examples/people.json"

# this is opening up the file to be read from
opened_file = open(file_path, "r")
print(opened_file)      # this only gives info about the file

# .read() - this actually reads the data inside the file
file_text = opened_file.read()
print(file_text)        # this is a string with all the text that was in the file

# anytime you open a file, you need to make sure to close it
# ONLY CLOSE YOUR FILE WHEN YOU'RE DONE WITH IT
# .close() - can be used to close the opened file
opened_file.close()


# we need to convert this JSON text, into usuable varaibles
# loads() is from the JSON module - it converts json text into python variables
people = loads(file_text)
print(people)

for p in people :
    print(p.get("name"))
    print(p.get("age"))
    print(p.get("height"))


# There is a statement in python, that will open your file, 
# and AUTOMATICALLY close it for you when its done.
# with statement 
with open(file_path, "r") as input_file :
    text = input_file.read()

print(text)




# the file we will be working with
file_name = "C:\VetTec_Python\Day5_examples\people2.json"


# converting a list of dictionaries into a JSON string
# using the dumps function that was imported from the JSON module
json_str = dumps(people)


# writing to a file
with open(file_name, "w") as output_file :
    
    # .write() takes in a string, and puts the text in the file
    output_file.write(json_str)


# writing will override EVERYTHING thats currently in the specified file
# append will add to the end of whatever is in the file


file_name = "C:/VetTec_Python/Day5_examples/append_test.txt"

# appending to a file
with open(file_name, "a") as output_file :
    
    # still, we use the .write() function and pass in a string
    # the file is opened for append operations, so python will handle that
    output_file.write("Now, I'm adding more text! Fun!!")



# creating a file

# this is the file we WANT to create
file_name = "C:/VetTec_Python/Day5_examples/people3.json"

try :
    with open(file_name, "x") as new_file :
        
        # writing the JSON string of people info to the newly created file
        new_file.write(json_str)
except FileExistsError :
    
    # if the given file already exists, go ahead and write to the file instead
    with open(file_name, "w") as output_file :
        output_file.write(json_str)



# OTHER POTENTIAL ERRORS

# io.UnsupportedOperation
# if you try to perform an operation the file wasn't opened for
#with open(file_name, "r") as in_file :
#    in_file.write()



# ValueError
# if you try to perform an operation on a closed file
#file = open(file_name, "r")
#file.close()

#file.read()     # this gives the ValueError



# FileNotFoundError
# if the specified file does not exist OR the file path incorrect

# ** YOU CAN USE THIS TO CHECK IF A GIVEN FILE IS CORRECT

while True :    
    file_name = input("Enter a file name:")

    try :
        with open(file_name, "r") as in_file :
            file_text = in_file.read()

        print("File data is being read...")
        break
    except FileNotFoundError :
        print("Sorry. Couldn't find that file. Try again.")