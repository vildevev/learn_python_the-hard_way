# imports the argv module
from sys import argv 

# assigns these variables to whatever is typed into the console
script, filename = argv 

# opens the file with the name provided at the argv
txt = open(filename)

# presents the filename
print(f"Here's your file {filename}:")
# prints out the content of the file
print(txt.read())

# prompts the user to type the name of the file again, stores the input as a variable
print("Type the filename again:")
file_again = input("> ")

# opens a file with the given name
txt_again = open(file_again)

# prints the content of this file
print(txt_again.read())

# using input is better since you can print out instructions to the user before. With argv the user is expected to know what to type, how many arguments etc. 

# you have to close the files 
txt_again.close()
txt.close()