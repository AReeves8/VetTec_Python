# OS MODULE

# importing the OS module
import os


# the OS module, gives you access to system commands in your code

working_directory = os.getcwd()
print("The current working directory is: " + str(working_directory))


# this will call ls on the given directory as a starting point
directories = os.listdir(working_directory)
for dir in directories :
    print(dir)




import subprocess
import sys


# the subprocess module allows you to start up subprocesses in your python program
# the sys module gives you access to python system variables


script_to_run = "C:/VetTec_Python/Day1_examples/variables_and_types.py"

# .run() takes in a list, where the first item is your executable, and the 2nd item is the file
# it takes each item in a list, and builds out a command to run the program
#   python3 variables_and_types.py
subprocess.run([sys.executable, script_to_run])

# sys.executable above is grabbing the location of your python installation


# you can also use this, to run bash scripts
# YOU NEED TO BE IN LINUX TO RUN YOUR BASH SCRIPTS
# if you run a bash script, and that script has a shebang, then you DON'T NEED shell=True
echo_output = subprocess.run(["echo", "Running a bash command!"], shell=True)
print(echo_output)