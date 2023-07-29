"""1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file. """
FILENAME = "name.txt"
user_name = input("Please enter your name: ")
with open(FILENAME, 'w') as out_file:
    print(user_name, file=out_file)

"""2. Write code that opens "name.txt" and reads the name (as above) then prints,
Your name is Bob"""

with open(FILENAME) as in_file:
    name = in_file.read().strip()
    print(f"Your name is {name}")