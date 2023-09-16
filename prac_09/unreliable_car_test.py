"""
CP1404 - Programming 2
UnreliableCar Class
Name: Doa Ngoc Tuan
Start from: 10:31 am  - Sat 16 Sep 2023
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    first_unreliable_car = UnreliableCar(name="Austin", fuel=80, reliability=100)
    first_unreliable_car.drive(50)
    print(first_unreliable_car)

    second_unreliable_car = UnreliableCar(name="Andrew", fuel=160, reliability=50)
    second_unreliable_car.drive(90)
    print(second_unreliable_car)


main()
