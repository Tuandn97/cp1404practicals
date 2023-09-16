"""
CP1404/CP5632 Practical 9
Taxi client file
Name: Dao Ngoc Tuan
Start time: 3.00 pm
End time:
"""

from prac_09.car import Car
from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"Taxi's details:{my_taxi},\nThe current fare: ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Taxi's details:{my_taxi},\nThe current fare ${my_taxi.get_fare()}")


main()


