"""
CP1404 - Programming 2
SilverServiceTaxi Class
Name: Doa Ngoc Tuan
Start from: 10:46 am  - Sat 16 Sep 2023
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Main SilverServiceTaxi Class"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialize a SilverServiceTaxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of SilverServiceTaxi"""
        return f"{super().__str__()} ${self.fanciness:.2f}/km plus flag-fall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the fare for the taxi ride, including flagfall"""
        return super().get_fare() + self.flagfall
