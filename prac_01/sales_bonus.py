"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MIN_SALES = 0
MAX_SALES = 1000
LOW_RATE = 0.1
HIGH_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= MIN_SALES:
    if sales < MAX_SALES:
        bonus = sales * LOW_RATE
    else:
        bonus = sales * HIGH_RATE
    print(f"Your bonus is {bonus}")
    sales = float(input("Enter sales: $"))
print(f"Invalid input")
