"""1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file. """
FILENAME = "name.txt"
user_name = input("Please enter your name: ")
with open(FILENAME, 'w') as out_file:
    print(user_name, file=out_file)

