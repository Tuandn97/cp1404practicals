"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MAX_SCORE = 100
MIN_SCORE = 0

import random


def main():
    score = float(input("Enter score: "))
    message = determine_score(score)
    print(message)
    random_score = random.randint(1, 100)
    message2 = determine_score(random_score)
    print(f"The random score is {random_score} which is {message2}")


def determine_score(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()
