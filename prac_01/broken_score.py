"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MAX_SCORE = 100
MIN_SCORE = 0

score = float(input("Enter score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")