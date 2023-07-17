MINIMUM_CHAR = 0

password = input("Enter your password: ")

while len(password) <= MINIMUM_CHAR:
    print("Invalid Password")
    password = input("Enter your password: ")
print("*" * len(password))
