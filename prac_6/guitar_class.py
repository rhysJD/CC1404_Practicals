"""
CP1404 - Practical 6
Rhys Donaldson
"""


class guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
