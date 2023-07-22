"""
CP1404 - Practical
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print("Thank You!")
        elif choice == "P":
            result = determine_score(score)
            print(f" Your result is: {result}")
        elif choice == "S":
            for i in range(score):
                print("*", end="")
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>>").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter a score (0-100): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score. Please enter a score between 0 and 100 inclusive.")
        score = int(input("Enter your score:"))
    return score


def determine_score(score):
    if score >= EXCELLENT_SCORE:
        message = "Excellent"
    elif score >= PASSABLE_SCORE:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()
