MINIMUM_CHAR = 0


def main():
    password = get_password()
    display_password(password)


def display_password(password):
    """Print the password"""
    print("*" * len(password))


def get_password():
    """get and validate the password"""
    password = input("Enter your password: ")
    while len(password) <= MINIMUM_CHAR:
        print("Invalid Password")
        password = input("Enter your password: ")
    return password


main()
