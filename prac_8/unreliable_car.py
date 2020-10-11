"""
Practical 8 CP1404
Rhys Donaldson
13581558
"""

from prac_8.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Checks if the car will drive then drives it"""
        if random.randrange(1, 100) > (100 - self.reliability):
            return super().drive(distance)
        else:
            return "Car broke down and drove 0km"
