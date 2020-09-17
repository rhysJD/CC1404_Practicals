"""
Practical 6
Rhys Donaldson
"""

from prac_6.guitar_class import guitar

gibson = guitar("Gibson L-5 CES", 1922, 16035.40)

other = guitar("TRASH", 2013, 30)

print(other.get_age())
print(gibson.get_age())
