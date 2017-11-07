# set a variable with a value of 10
types_of_people = 10 
# sets variable x to first part of joke
x = f"There are {types_of_people} types of people."

# sets binary variable
binary = "binary"
# sets do not variable
do_not = "don't"

# inserts the variables into string
y = f"Those who know {binary} and those who {do_not}."

# print out the jokes
print(x)
print(y)

# repeats them, interpolating them into strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set varible with value of False
hilarious = False 
# create string with empty interpolation
joke_evaluation = "Isn't that joke so funny?! {}"

# uses .format method to insert variable
print(joke_evaluation.format(hilarious))

# create two variables
w = "This is the left side of..."
e = "a string with a right side."

# add them together and prints them out
# only works if they're the same type ex. strings, integers etc. 
print(w + e)