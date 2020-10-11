"""
Practical 8 CP1404
Rhys Donaldson
13581558
"""

from prac_8.taxi import Taxi


def main():
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    print(prius_1.__str__())
    print(prius_1.get_fare())

    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1.__str__())
    print(prius_1.get_fare())

main()
