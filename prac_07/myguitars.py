"""
CP1404/CP5632 Practical 7 - Client code to use the Guitar  class.
Estimate: 20 minutes
Actual:    minutes
"""
from prac_07.guitar import Guitar

guitars = []
with open('guitars.csv') as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        guitars.sort()

for guitar in guitars:
    print(guitar)
