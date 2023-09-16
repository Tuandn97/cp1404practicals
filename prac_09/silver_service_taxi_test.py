"""
CP1404 - Programming 2
SilverServiceTaxi Client
Name: Doa Ngoc Tuan
Start from: 11:30 am  - Sat 16 Sep 2023
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    test_silver_taxi = SilverServiceTaxi("Austin", 100, 2)
    test_silver_taxi.drive(18)
    print(test_silver_taxi)
    print(f"The fare for a 80km trip is ${test_silver_taxi.get_fare()}.")


main()
