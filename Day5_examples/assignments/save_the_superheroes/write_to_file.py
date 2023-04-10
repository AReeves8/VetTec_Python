# this function writes data to a given file. if the file doesn't exist, it will create the file
# the function takes in 2 params. 1 for the name of the file and one for a string of data
# this function does not return anything
def write_to_file(file_name, json_str) :
    
    # if the file already exists, override it
    try :
        # trying to create the given file and write the JSON data to it
        with open(file_name, "x") as output_file :
            output_file.write(json_str)
    except FileExistsError:

        # if the given file already exists, override it
        with open(file_name, "w") as output_file :
            output_file.write(json_str)

