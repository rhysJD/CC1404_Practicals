"""
CP1404 Practical 6
Rhys Donaldson
"""
# Note that the import has a folder (module) in it.

from prac_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(100)
    my_car.drive(30)
    my_car.add_fuel(0)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(str(my_car))

main()