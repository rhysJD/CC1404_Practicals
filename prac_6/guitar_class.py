"""
CP1404 - Practical 6
Rhys Donaldson
"""

class guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        if get_age(self) >= 50:
            return True
        else:
            return False

        

