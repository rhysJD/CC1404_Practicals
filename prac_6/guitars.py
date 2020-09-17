"""
Practical 6
Rhys Donaldson
"""

from prac_6.guitar_class import guitar
print("My Guitars!")

guitars = []

store_name = input('Name: ')
while store_name != "":
    store_year = input("Year: ")
    store_cost = input("Cost: ")
    store = guitar(store_name, store_year, store_cost)
    guitars.append(store)
    store_name = input('Name: ')
guitars.append(guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
#
