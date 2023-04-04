#[1]
#Our system calcualtes the number of seconds it took to load in some data and displays it to the user.
#The data is being stored with a decimal place, but we want to make sure we only display a whole number back to the user.
load_time = 4.87
load_time_int = int(load_time)
print("The load time for the data was " + str(load_time_int) + " seconds.")


#[2]
#We have this variable that is storing the name of a product from our database, but the string is being formatted incorrectly by our system. 
#We want to make sure the string is uniform before displaying it back to the user. 
product_name = "ReD ziPpEr hOOdiE"
print("Product Name: " + product_name.title())


#[3]
#Our database contains all the movies that a person has rented, but each movie is separated by a comma. 
#We need to remove the commas and substitute them for empty spaces before they can move on for further processing.  
rental_history = "Avengers: Endgame, The Notebook, Napoleon Dynamite"
rental_history_formatted = rental_history.replace(",", " ")
print("Formatted rental history: " + rental_history_formatted)


#[4] 
#Currently we have 2 variables that are storing a basketball player's name and number of points they scored. 
#Print both of these variables out in a single print statement that is also formatted to be a logical English sentence.
player_name = "Luka Doncic"
player_points = 32
print(player_name + " scored " + str(player_points) + " points in last night's game.")


#[5]
#We want to ask the user to give us any piece of data and report back to them the data type of whatever they gave us. 
user_input = input("Submit any piece of data and I will tell you what type it is: ")

# user_input will ALWAYS be a string - so for now, this doesn't actually work the way that it should
print("'" + str(user_input) + "' has the following type: " + str(type(user_input)))     

#[6] 
#We want to prompt the user to input their first and last name (using separate input() statements) and then report back to them the number of characters in their full name. 
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
total_characters = len(user_first_name) + len(user_last_name)
print("Your full name has " + str(total_characters) + " characters in it.")

#[7]
#This one actually doesn't require the use of a function. var1 and var2 each are assigned a value.
#You need to swap the values of var1 and var2 only using variables and print the results. Do not directly assign these a new value, they must be assigned to a variable. 
var1 = 20
var2 = "a different value"

temp = var1
var1 = var2
var2 = temp

print("var1 = " + str(var1))
print("var2 = " + str(var2))