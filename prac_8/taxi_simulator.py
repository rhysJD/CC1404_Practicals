"""
Practical 8 CP1404
Rhys Donaldson
13581558
"""
from prac_8.silver_service_taxi import SilverServiceTaxi
from prac_8.taxi import Taxi

current_taxi = None
current_total = 0

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
choice = input("Let's drive! \n q)uit, c)hoose, d)rive \n >>> ")
while choice is not "q":
    if choice == "c":
        print("Taxis available")
        for i, taxi in enumerate(taxis):
            print("{} - {}".format(i, taxi.__str__()))
        current_taxi = taxis[int(input("Choose taxi:"))]
    elif choice == "d":
        current_taxi.drive(int(input("Drive how far?")))
        current_total += current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f} \nBill to date: ${:.2f}".format(current_taxi.name, current_taxi.get_fare(), current_total))
        current_taxi.start_fare()
    else:
        print("That is not an option.")

    choice = input("\nq)uit, c)hoose, d)rive \n >>>")

print("Total trip cost: ${:.2f} \nTaxis are now:".format(current_total))
for i, taxi in enumerate(taxis):
    print("{} - {}".format(i, taxi.__str__()))