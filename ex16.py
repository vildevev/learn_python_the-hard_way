from sys import argv 

script, filename = argv 

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you don't want that, hit RETURN.")

input("?")

print("Opening the file...")
# opens the file, truncates (empties) file if it already exists. Overwrites with whatever comes after. 
# 'r' parameter is the default
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# empties file, but with 'w' parameter this is redundant.
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# adds the user input to file on separate lines.
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
# 'saves' the file
target.close()

# open and reads content of file
print(open(filename).read())
