"""
CP1404 - Programming 2
SilverServiceTaxi Class
Name: Doa Ngoc Tuan
Start from: 10:46 am  - Sat 16 Sep 2023
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Main of SilverServiceTaxi Class"""
    flag_fall = 4.50

    def __init(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string for SilverServiceTaxi class   """
        return f"{super().__init__} ${self.fanciness}/km plus flag-fall of {self.flag_fall}"

    def __get_fare__(self):
        """Add flag_all to the fare"""
        return super().get_fare() + self.flag_fall
