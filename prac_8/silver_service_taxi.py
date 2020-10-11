"""
Practical 8 CP1404
Rhys Donaldson
13581558
"""
from prac_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi service"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialised values"""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Calculates the fare using the old function and adding flag fall"""
        fare = super().get_fare() + self.flagfall
        return fare
