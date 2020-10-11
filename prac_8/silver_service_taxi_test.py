"""
Practical 8 CP1404
Rhys Donaldson
13581558
"""
from prac_8.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
fancy_taxi.drive(18)
print("${:.2f}".format(fancy_taxi.get_fare()))
print(fancy_taxi.__str__())