"""
CP1404 - Programming 2
UnreliableCar Class
Name: Doa Ngoc Tuan
Start from: 10:20 am  - Sat 16 Sep 2023
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCari instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a UnreliableCari information"""
        return f"{super().__str__()}, the car's reliability:  {self.reliability}."

    def __drive__(self, distance):
        """Determine drive car or not base on breakdown_chance"""
        breakdown_chance = random.randint(0, 100)
        if breakdown_chance < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
