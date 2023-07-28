"""CP1404/CP5632 - Practical Answer the following questions: o
1. When will a ValueError occur? When the user enters a
value that cannot be converted to an integer (string included)
2. When will a ZeroDivisionError occur? When the value
entered by the user for the denominator is 0, cannot be divided by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By adding a check for the denominator before doing the division, we can alter the
code to prevent the chance of a ZeroDivisionError. The code will be upload below """

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")